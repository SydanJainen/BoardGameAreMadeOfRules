import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


class TemplateError(Exception):
    pass


class TemplateNotFoundError(TemplateError):

    def __init__(self, file_path: str):
        self.file_path = file_path
        super().__init__(f"Template file not found: {file_path}")


class TemplateParseError(TemplateError):

    def __init__(self, message: str, line_number: Optional[int] = None):
        self.line_number = line_number
        if line_number is not None:
            super().__init__(f"Template parse error at line {line_number}: {message}")
        else:
            super().__init__(f"Template parse error: {message}")


class TemplateValidationError(TemplateError):

    def __init__(self, message: str, errors: Optional[List] = None):
        self.errors = errors or []
        super().__init__(message)

    def __str__(self):
        if not self.errors:
            return self.args[0]

        error_lines = [self.args[0]]
        for err in self.errors:
            severity = err.severity.upper() if hasattr(err, "severity") else "ERROR"
            field = err.field if hasattr(err, "field") else "unknown"
            message = err.message if hasattr(err, "message") else str(err)
            error_lines.append(f"  [{severity}] {field}: {message}")

        return "\n".join(error_lines)


class TemplateContentError(TemplateError):

    def __init__(self, message: str, file_path: Optional[str] = None):
        self.file_path = file_path
        if file_path:
            super().__init__(f"Template content error: {message} (file: {file_path})")
        else:
            super().__init__(f"Template content error: {message}")


@dataclass
class ValidationError:
    field: str
    message: str
    severity: str = "error"


@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationError]


@dataclass
class TemplateData:
    command: str
    version: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    context: Dict[str, Any] = field(default_factory=dict)
    parameters: Dict[str, Any] = field(default_factory=dict)
    content: Dict[str, Any] = field(default_factory=dict)
    source_file: str = ""
    model: str = ""
    custom_prompt: str = ""
    prompt_file: str = ""


class TemplateValidator:

    VALID_COMMANDS = {"explain", "analyse", "fix-rules", "invent", "recommend-move"}
    VALID_AUDIENCES = {"child", "adult", "expert"}
    VALID_FORMATS = {"json", "markdown"}

    CONTENT_REQUIREMENTS = {
        "explain": ["rules", "rules_file"],
        "analyse": ["rules", "rules_file"],
        "fix-rules": ["rules", "rules_file"],
        "invent": ["concept", "idea_summary"],
        "recommend-move": ["rules", "rules_file", "game_state"],
    }

    def validate(self, template: dict) -> ValidationResult:
        errors = []
        warnings = []

        errors.extend(self._validate_structure(template))

        command = template.get("command")
        if command and command in self.VALID_COMMANDS:
            errors.extend(self._validate_content(template, command))
            errors.extend(self._validate_parameters(template, command))

        prompt_errors, prompt_warnings = self._validate_custom_prompt_fields(template)
        errors.extend(prompt_errors)
        warnings.extend(prompt_warnings)

        return ValidationResult(is_valid=len(errors) == 0, errors=errors, warnings=warnings)

    def _validate_structure(self, template: dict) -> List[ValidationError]:
        errors = []

        for fld in ["command", "version", "content"]:
            if fld not in template:
                errors.append(ValidationError(fld, f"Required field missing: {fld}"))

        command = template.get("command")
        if command and command not in self.VALID_COMMANDS:
            valid = ", ".join(sorted(self.VALID_COMMANDS))
            errors.append(ValidationError("command", f"Invalid command: '{command}'. Must be: {valid}"))

        version = template.get("version", "")
        if version and not re.match(r"^\d+\.\d+$", str(version)):
            errors.append(ValidationError("version", f"Invalid version format: '{version}'. Expected 'X.Y'"))

        model = template.get("model")
        if model is not None and (not isinstance(model, str) or not model.strip()):
            errors.append(ValidationError("model", "Model must be a non-empty string"))

        return errors

    def _validate_content(self, template: dict, command: str) -> List[ValidationError]:
        errors = []
        content = template.get("content", {})

        if command == "recommend-move":
            if "game_state" not in content:
                errors.append(ValidationError("content.game_state", "Content must contain 'game_state'"))
            if "rules" not in content and "rules_file" not in content:
                errors.append(ValidationError("content", "Content must contain 'rules' or 'rules_file'"))
        else:
            required_fields = self.CONTENT_REQUIREMENTS.get(command, [])
            if required_fields and not any(fld in content for fld in required_fields):
                field_list = "' or '".join(required_fields)
                errors.append(ValidationError("content", f"Content must contain '{field_list}'"))

        return errors

    def _validate_parameters(self, template: dict, command: str) -> List[ValidationError]:
        errors = []
        params = template.get("parameters", {})

        fmt = params.get("format")
        if fmt and fmt not in self.VALID_FORMATS:
            errors.append(ValidationError("parameters.format", f"Invalid format: '{fmt}'"))

        if command == "explain":
            audience = params.get("audience", "adult")
            if audience not in self.VALID_AUDIENCES:
                errors.append(ValidationError("parameters.audience", f"Invalid audience: '{audience}'"))

            level = params.get("simplification_level")
            if level is not None:
                try:
                    if not (1 <= int(level) <= 5):
                        errors.append(ValidationError("parameters.simplification_level", f"Must be 1-5, got: {level}"))
                except (ValueError, TypeError):
                    errors.append(ValidationError("parameters.simplification_level", f"Must be a number, got: {level}"))

        elif command == "analyse":
            bgg_id = params.get("bgg_id")
            if bgg_id is not None:
                try:
                    if int(bgg_id) <= 0:
                        errors.append(ValidationError("parameters.bgg_id", f"Must be positive, got: {bgg_id}"))
                except (ValueError, TypeError):
                    errors.append(ValidationError("parameters.bgg_id", f"Must be a number, got: {bgg_id}"))

        elif command == "invent":
            complexity = params.get("complexity")
            if complexity is not None:
                try:
                    if not (1.0 <= float(complexity) <= 5.0):
                        errors.append(ValidationError("parameters.complexity", f"Must be 1.0-5.0, got: {complexity}"))
                except (ValueError, TypeError):
                    errors.append(ValidationError("parameters.complexity", f"Must be a number, got: {complexity}"))

        return errors

    def _validate_custom_prompt_fields(self, template: dict):
        errors = []
        warnings = []

        custom_prompt = template.get("custom_prompt")
        prompt_file = template.get("prompt_file")

        if custom_prompt is not None and not isinstance(custom_prompt, str):
            errors.append(
                ValidationError("custom_prompt", "custom_prompt must be a string", severity="error")
            )

        if prompt_file is not None and not isinstance(prompt_file, str):
            errors.append(
                ValidationError("prompt_file", "prompt_file must be a string", severity="error")
            )

        if custom_prompt and prompt_file:
            warnings.append(
                ValidationError(
                    "custom_prompt",
                    "Both custom_prompt and prompt_file are set. prompt_file takes priority.",
                    severity="warning",
                )
            )

        return errors, warnings


class TemplateLoader:

    @staticmethod
    def load(file_path: str) -> TemplateData:
        path = Path(file_path)

        if not path.exists():
            raise TemplateNotFoundError(file_path)
        suffix = path.suffix.lower()

        try:
            if suffix == ".md":
                return TemplateLoader.load_markdown_template(file_path)
            elif suffix in [".yaml", ".yml"]:
                return TemplateLoader.load_yaml_template(file_path)
            else:
                raise TemplateParseError(
                    f"Unsupported template format: {suffix}. Use .md, .yaml, or .yml"
                )
        except (yaml.YAMLError, ImportError) as e:
            raise TemplateParseError(f"Failed to parse template: {e}")

    @staticmethod
    def load_markdown_template(file_path: str) -> TemplateData:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()

            frontmatter_pattern = r"^---\s*\n(.*?)\n---\s*\n?(.*)$"
            match = re.match(frontmatter_pattern, file_content, re.DOTALL)

            if not match:
                raise TemplateParseError(
                    "Invalid Markdown template: missing YAML frontmatter. "
                    "Template must start with '---' followed by YAML content and closing '---'"
                )

            yaml_content = match.group(1)
            markdown_body = match.group(2).strip()

            try:
                raw_data = yaml.safe_load(yaml_content)
            except yaml.YAMLError as e:
                raise TemplateParseError(f"YAML frontmatter syntax error: {e}")

            if not isinstance(raw_data, dict):
                raise TemplateParseError(
                    "Template frontmatter must be a YAML dictionary/object"
                )

            if "content" in raw_data:
                content = raw_data["content"]
                if isinstance(content, dict):
                    if "rules" not in content and markdown_body:
                        content["rules"] = markdown_body
                else:
                    raw_data["content"] = {"rules": markdown_body}
            else:
                if markdown_body:
                    raw_data["content"] = {"rules": markdown_body}
                else:
                    raw_data["content"] = {}

            return TemplateLoader._parse_and_validate(raw_data, file_path)

        except Exception as e:
            if isinstance(e, (TemplateParseError, TemplateValidationError)):
                raise
            raise TemplateParseError(f"Failed to load Markdown template: {e}")

    @staticmethod
    def load_yaml_template(file_path: str) -> TemplateData:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_data = yaml.safe_load(f)

            if not isinstance(raw_data, dict):
                raise TemplateParseError("Template must be a YAML dictionary/object")

            return TemplateLoader._parse_and_validate(raw_data, file_path)

        except yaml.YAMLError as e:
            raise TemplateParseError(f"YAML syntax error: {e}")
        except Exception as e:
            if isinstance(e, (TemplateParseError, TemplateValidationError)):
                raise
            raise TemplateParseError(f"Failed to load YAML template: {e}")

    @staticmethod
    def _parse_and_validate(raw_data: dict, source_file: str) -> TemplateData:
        validator = TemplateValidator()
        result = validator.validate(raw_data)

        if not result.is_valid:
            error_messages = []
            for err in result.errors:
                error_messages.append(
                    f"  [{err.severity.upper()}] {err.field}: {err.message}"
                )

            raise TemplateValidationError(
                "Template validation failed:\n" + "\n".join(error_messages),
                errors=result.errors,
            )
        return TemplateData(
            command=raw_data["command"],
            version=raw_data["version"],
            metadata=raw_data.get("metadata", {}),
            context=raw_data.get("context", {}),
            parameters=raw_data.get("parameters", {}),
            content=raw_data.get("content", {}),
            source_file=source_file,
            model=raw_data.get("model", ""),
            custom_prompt=raw_data.get("custom_prompt", ""),
            prompt_file=raw_data.get("prompt_file", ""),
        )
