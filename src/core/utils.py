import json
import logging
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

import yaml

from src.core.models import (
    AnalysisResult,
    ExplanationResult,
    FixRulesResult,
    InventResult,
    MoveRecommendation,
)

logger = logging.getLogger(__name__)



class TextCleaner:
    def __init__(
        self,
        remove_page_numbers: bool = True,
        remove_headers: bool = True,
        clean_spaces: bool = True,
    ):

        self.remove_page_numbers = remove_page_numbers
        self.remove_headers = remove_headers
        self.clean_spaces = clean_spaces

    def preprocess(self, text: str) -> str:

        result = text

        if self.remove_page_numbers:
            result = self._strip_page_nums(result)

        if self.remove_headers:
            result = self._remove_headers(result)

        if self.clean_spaces:
            result = self._clean_spaces(result)

        return result.strip()

    def _strip_page_nums(self, text: str) -> str:

        return re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

    def _remove_headers(self, text: str) -> str:

        lines = text.split("\n")
        cleaned = []

        for line in lines:
            stripped = line.strip()
            if stripped.isupper() and len(stripped) < 50 and len(stripped) > 0:
                if stripped.endswith(":"):
                    cleaned.append(line)
                    continue
                continue
            cleaned.append(line)

        return "\n".join(cleaned)

    def _clean_spaces(self, text: str) -> str:
        result = re.sub(r" +", " ", text)
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result



PLACEHOLDER_NAMES = {"Untitled Game", "New Game", "TBD", "Game"}

PLACEHOLDER_THEMES = {"TBD", "None", "N/A"}


def validate_game_name(name: str) -> Tuple[bool, str]:
    if not name or not name.strip():
        return False, "Game name is empty"

    name_stripped = name.strip()

    if len(name_stripped) <= 5:
        return False, f"Game name too short: '{name_stripped}'"

    if name_stripped in PLACEHOLDER_NAMES:
        return False, f"Game name is placeholder: '{name_stripped}'"

    return True, ""


def validate_theme(theme: str) -> Tuple[bool, str]:
    if not theme or not theme.strip():
        return False, "Theme is empty"

    theme_stripped = theme.strip()

    if len(theme_stripped) <= 10:
        return False, f"Theme too short: '{theme_stripped}'"

    if theme_stripped in PLACEHOLDER_THEMES:
        return False, f"Theme is placeholder: '{theme_stripped}'"

    return True, ""


def validate_mechanics(mechanics: List[str]) -> Tuple[bool, str]:
    if not mechanics:
        return False, "Mechanics list is empty"

    if len(mechanics) < 2:
        return False, f"Insufficient mechanics: {len(mechanics)} (need >= 2)"

    for i, mechanic in enumerate(mechanics):
        if not mechanic or not mechanic.strip():
            return False, f"Mechanic #{i+1} is empty"

        if len(mechanic.strip()) <= 5:
            return (
                False,
                f"Mechanic #{i+1} too short: '{mechanic.strip()}' (must be > 5 chars)",
            )

    return True, ""


def validate_components(components: List[str]) -> Tuple[bool, str]:
    if not components:
        return False, "Components list is empty"

    if len(components) < 3:
        return False, f"Insufficient components: {len(components)} (need >= 3)"

    for i, component in enumerate(components):
        if not component or not component.strip():
            return False, f"Component #{i+1} is empty"

        if len(component.strip()) <= 3:
            return (
                False,
                f"Component #{i+1} too short: '{component.strip()}' (must be > 3 chars)",
            )

    return True, ""


def validate_board_game(game_dict: dict) -> Tuple[bool, str]:
    validators: List[Tuple[str, Callable[[Any], Tuple[bool, str]], Any]] = [
        ("game_name", validate_game_name, game_dict.get("game_name", "")),
        ("theme", validate_theme, game_dict.get("theme", "")),
        ("mechanics", validate_mechanics, game_dict.get("mechanics", [])),
        ("components", validate_components, game_dict.get("components", [])),
    ]

    errors = []
    for field_name, validator, value in validators:
        is_valid, error_msg = validator(value)
        if not is_valid:
            errors.append(f"{field_name}: {error_msg}")

    if errors:
        return False, "; ".join(errors)

    return True, ""


class UnifiedParser:
    def parse(self, response: str, target_model: type) -> dict:
        if self._looks_like_json(response):
            result = self._try_json_parse(response)
            if result and self._is_valid_result(result):
                return result

        result = self._parse_structured(response)
        if result and self._is_valid_result(result):
            return result

        return self._create_fallback_dict(response)

    def get_format_instructions(self) -> str:
        return """
OUTPUT FORMAT (choose one):

Option 1 - JSON:
{
  "game_name": "Name",
  "theme": "Description",
  "mechanics": ["mechanic1", "mechanic2"],
  "components": ["component1", "component2"],
  "players": "2-4",
  "duration": "60 minutes",
  "rules": {
    "setup": "Setup instructions",
    "gameplay": "Turn structure",
    "winning_condition": "How to win"
  }
}

Option 2 - Structured Text:
GAME NAME: Name
THEME: Description
MECHANICS: mechanic1, mechanic2
COMPONENTS: component1, component2
PLAYERS: 2-4
DURATION: 60 minutes

SETUP:
[Setup instructions]

GAMEPLAY:
[Turn structure]

WINNING CONDITION:
[How to win]
""".strip()

    def _create_fallback_dict(
        self, response: str, defaults: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        base_defaults = {
            "name": "Untitled Game",
            "game_name": "Untitled Game",
            "theme": "",
            "mechanics": [],
            "components": [],
            "players": "2-4",
            "player_count": "2-4",
            "duration": "60 minutes",
            "rules": response.strip() if response.strip() else "No rules generated",
        }

        if defaults:
            base_defaults.update(defaults)

        return base_defaults

    def _safe_split_list(self, text: str, separator: str = ",") -> list:
        if not text or not text.strip():
            return []

        return [item.strip() for item in text.split(separator) if item.strip()]

    def _looks_like_json(self, text: str) -> bool:
        stripped = text.strip()
        return stripped.startswith("{") and ":" in stripped and "}" in stripped

    def _try_json_parse(self, response: str) -> Optional[dict]:
        json_text = self._extract_json_block(response)
        if not json_text:
            return None

        try:
            data = json.loads(json_text)
            return self._convert_to_flat_format(data, response)
        except json.JSONDecodeError:
            return None

    def _extract_json_block(self, text: str) -> Optional[str]:
        text = re.sub(r"```json\s*", "", text)
        text = re.sub(r"```\s*", "", text)

        brace_count = 0
        start_idx = None

        for i, char in enumerate(text):
            if char == "{":
                if brace_count == 0:
                    start_idx = i
                brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0 and start_idx is not None:
                    return text[start_idx : i + 1]

        return None

    def _convert_to_flat_format(self, data: dict, original_response: str) -> dict:
        result = {
            "name": data.get("game_name") or data.get("name", "Untitled Game"),
            "game_name": data.get("game_name") or data.get("name", "Untitled Game"),
            "theme": data.get("theme", ""),
            "mechanics": data.get("mechanics", []),
            "components": data.get("components", []),
            "players": data.get("players") or data.get("player_count", "2-4"),
            "player_count": data.get("player_count") or data.get("players", "2-4"),
            "duration": data.get("duration", "60 minutes"),
            "rules": "",
        }

        if isinstance(data.get("rules"), dict):
            rules_parts = []
            for section in ["setup", "gameplay", "winning_condition", "winning"]:
                if section in data["rules"]:
                    rules_parts.append(data["rules"][section])
            result["rules"] = "\n\n".join(rules_parts) if rules_parts else ""
        elif isinstance(data.get("rules"), str):
            result["rules"] = data["rules"]

        if not result["rules"] and original_response.strip():
            result["rules"] = original_response.strip()

        return result

    def _parse_structured(self, response: str) -> dict:
        result = {
            "name": "Untitled Game",
            "game_name": "Untitled Game",
            "theme": "",
            "mechanics": [],
            "components": [],
            "players": "2-4",
            "player_count": "2-4",
            "duration": "60 minutes",
            "rules": "",
        }

        game_name = self._extract_game_name(response)
        if game_name:
            result["name"] = game_name
            result["game_name"] = game_name

        theme = self._extract_field(response, ["theme"])
        if theme:
            result["theme"] = theme

        mechanics = self._extract_list_field(response, ["mechanics", "game mechanics"])
        if mechanics:
            result["mechanics"] = mechanics

        components = self._extract_list_field(response, ["components", "game components"])
        if components:
            result["components"] = components

        players = self._extract_field(response, ["players", "player count"])
        if players:
            result["players"] = players
            result["player_count"] = players

        duration = self._extract_field(response, ["duration", "play time", "playing time"])
        if duration:
            result["duration"] = duration

        rules = self._extract_rules(response)
        if rules:
            result["rules"] = rules
        elif response.strip():
            result["rules"] = response.strip()

        return result

    def _extract_game_name(self, text: str) -> Optional[str]:
        patterns = [
            r'\*\*\s*Game\s+Name\s*:\*\*\s*(.+?)(?:\n|$)',
            r'Game\s+Name\s*:\s*["\']?([^"\'\n]+)["\']?',
            r"^\s*#\s+([^#\n]+?)(?:\n|$)",
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
            if match:
                return match.group(1).strip().strip('"').strip("'")

        return None

    def _extract_field(self, text: str, field_names: list) -> Optional[str]:
        for field_name in field_names:
            patterns = [
                rf'\*\*\s*{field_name}\s*:\*\*\s*(.+?)(?:\n|$)',
                rf'##\s+{field_name}\s*\n\s*(.+?)(?:\n|$)',
                rf'{field_name}\s*:\s*(.+?)(?:\n|$)',
            ]

            for pattern in patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    value = match.group(1).strip().strip('"').strip("'")
                    if value:
                        return value

        return None

    def _extract_list_field(self, text: str, field_names: list) -> list:
        for field_name in field_names:
            section_text = self._extract_field_section(text, field_name)
            if not section_text:
                continue

            if "," in section_text:
                return self._safe_split_list(section_text, ",")

            numbered_items = re.findall(r"\d+\.\s*\*?\*?([^:\n]+)", section_text)
            if numbered_items:
                return [item.strip().strip("*").strip() for item in numbered_items]

            bullet_items = re.findall(r"[-*]\s+(.+?)(?:\n|$)", section_text)
            if bullet_items:
                return [item.strip() for item in bullet_items]

        return []

    def _extract_field_section(self, text: str, field_name: str) -> Optional[str]:
        patterns = [
            rf'(?:^|\n)\s*\*\*\s*{field_name}\s*:\*\*\s*(.*?)(?=\n\s*\*\*[A-Z][A-Z\s]+:\*\*|\n##|\Z)',
            rf'##\s+{field_name}\s*\n(.*?)(?=##|\Z)',
            rf'(?:^|\n)\s*{field_name}\s*:\s*(.*?)(?=\n[A-Z][A-Z\s]+:|\Z)',
        ]

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()

        return None

    def _extract_rules(self, response: str) -> str:
        rules_lines = []
        in_rules = False

        for line in response.split("\n"):
            line_stripped = line.strip()
            line_upper = line_stripped.upper()

            if self._is_rules_header(line_upper):
                in_rules = True
                rules_lines.append(line_stripped)
            elif in_rules:
                if self._is_non_rules_header(line_upper):
                    break
                rules_lines.append(line)

        if rules_lines:
            return "\n".join(rules_lines).strip()

        return ""

    def _is_rules_header(self, line_upper: str) -> bool:
        rules_headers = [
            "SETUP:", "GAMEPLAY:", "WINNING CONDITION:", "WINNING:",
            "RULES:", "GAME RULES:", "HOW TO PLAY:",
        ]

        for header in rules_headers:
            if line_upper.startswith(header) or line_upper.startswith("## " + header.rstrip(":")):
                return True
            if line_upper.startswith("**" + header):
                return True

        return False

    def _is_non_rules_header(self, line_upper: str) -> bool:
        non_rules = ["MECHANICS:", "COMPONENTS:", "THEME:", "PLAYERS:", "DURATION:"]
        return any(line_upper.startswith(h) for h in non_rules)

    def _is_valid_result(self, result: dict) -> bool:
        if not result.get("rules") or not result["rules"].strip():
            return False

        has_name = result.get("game_name") and result["game_name"] != "Untitled Game"
        has_theme = result.get("theme") and result["theme"].strip()
        has_mechanics = result.get("mechanics") and len(result["mechanics"]) > 0
        has_components = result.get("components") and len(result["components"]) > 0

        return has_name or has_theme or has_mechanics or has_components



class JSONFormatter:
    @staticmethod
    def format(result: Any) -> str:
        if hasattr(result, "model_dump"):
            data = result.model_dump(mode="json", exclude_none=True)
            return json.dumps(data, indent=2, ensure_ascii=False)
        elif hasattr(result, "__dict__"):
            data = JSONFormatter._to_dict(result)
            return json.dumps(data, indent=2, ensure_ascii=False)
        return json.dumps(result, indent=2, ensure_ascii=False)

    @staticmethod
    def save(result: Any, file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(JSONFormatter.format(result))

    @staticmethod
    def _to_dict(obj: Any) -> Any:
        if hasattr(obj, "__dict__"):
            result = {}
            for key, value in obj.__dict__.items():
                if value is None:
                    continue
                if hasattr(value, "__dict__"):
                    result[key] = JSONFormatter._to_dict(value)
                elif isinstance(value, list):
                    result[key] = [
                        JSONFormatter._to_dict(item) if hasattr(item, "__dict__") else item
                        for item in value
                    ]
                elif hasattr(value, "value"):  # Enum
                    result[key] = value.value
                else:
                    result[key] = value
            return result
        return obj


class MarkdownFormatter:
    @staticmethod
    def format(result: Any) -> str:
        metadata_yaml = MarkdownFormatter._format_metadata(result)
        content = ""

        if isinstance(result, ExplanationResult):
            content = MarkdownFormatter._format_explanation(result)
        elif isinstance(result, AnalysisResult):
            content = MarkdownFormatter._format_analysis(result)
        elif isinstance(result, FixRulesResult):
            content = MarkdownFormatter._format_fix_rules(result)
        elif isinstance(result, InventResult):
            content = MarkdownFormatter._format_invent(result)
        elif isinstance(result, MoveRecommendation):
            content = MarkdownFormatter._format_move(result)
        else:
            content = str(result)

        if metadata_yaml:
            return f"---\n{metadata_yaml}---\n\n{content}"
        return content

    @staticmethod
    def _format_metadata(result: Any) -> str:
        if not hasattr(result, "execution_metadata") or result.execution_metadata is None:
            return ""

        metadata_dict = result.execution_metadata.to_yaml_dict()
        return yaml.dump(metadata_dict, default_flow_style=False, sort_keys=False)

    @staticmethod
    def save(result: Any, file_path: str):
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(MarkdownFormatter.format(result))

    @staticmethod
    def _format_explanation(result: ExplanationResult) -> str:
        md = f"""# Rule Explanation for {result.audience.value.capitalize()} Audience

{result.explanation}
"""
        if result.raw_response:
            md += "\n## Raw LLM Response\n<details>\n<summary>Click to expand raw response</summary>\n\n```\n" + result.raw_response + "\n```\n\n</details>\n"

        return md

    @staticmethod
    def _format_analysis(result: AnalysisResult) -> str:
        md = f"""# Game Analysis

## Predicted Properties
- **Mechanics**: {', '.join(result.mechanics)}
- **Complexity**: {result.complexity}/5.0
- **Players**: {result.min_players}-{result.max_players}
- **Duration**: {result.duration_min} minutes
"""

        if result.bgg_mechanics:
            md += f"""
## BoardGameGeek Comparison
- **BGG Mechanics**: {', '.join(result.bgg_mechanics)}
- **BGG Complexity**: {result.bgg_complexity}/5.0
- **BGG Players**: {result.bgg_players}
- **BGG Duration**: {result.bgg_duration} minutes
"""
            if result.mechanics_similarity is not None:
                md += f"""
## Accuracy Metrics
- **Mechanics Similarity**: {result.mechanics_similarity:.2%}
- **Complexity Error**: {result.complexity_error:.2f}
- **Overall Score**: {result.overall_score:.2%}
"""

        if result.raw_response:
            md += "\n## Raw LLM Response\n<details>\n<summary>Click to expand raw response</summary>\n\n```\n" + result.raw_response + "\n```\n\n</details>\n"

        return md

    @staticmethod
    def _format_fix_rules(result: FixRulesResult) -> str:
        md = """# Rule Analysis and Corrections

## Issues Identified
"""
        for i, issue in enumerate(result.identified_issues, 1):
            md += f"{i}. {issue}\n"

        md += "\n## Suggested Fixes\n"
        for i, fix in enumerate(result.suggested_fixes, 1):
            md += f"{i}. {fix}\n"

        md += f"""
## Corrected Rules

{result.corrected_rules}
"""
        if result.raw_response:
            md += "\n## Raw LLM Response\n<details>\n<summary>Click to expand raw response</summary>\n\n```\n" + result.raw_response + "\n```\n\n</details>\n"

        return md

    @staticmethod
    def _format_invent(result: InventResult) -> str:
        md = f"""# {result.game_name}

## Theme
{result.theme}

## Game Details
- **Mechanics**: {', '.join(result.mechanics)}
- **Players**: {result.player_count}
- **Duration**: {result.duration}

## Components
{chr(10).join(f"- {c}" for c in result.components)}

## Rules
{result.rules}
"""
        if result.raw_response:
            md += "\n## Raw LLM Response\n<details>\n<summary>Click to expand raw response</summary>\n\n```\n" + result.raw_response + "\n```\n\n</details>\n"

        return md

    @staticmethod
    def _format_move(result: MoveRecommendation) -> str:
        md = f"""# Move Recommendation

## Current Game State
{result.current_state}

## Recommended Move
{result.recommended_move}

## Reasoning
{result.reasoning}
"""
        if result.alternative_moves:
            md += "\n## Alternative Moves\n"
            for i, alt in enumerate(result.alternative_moves, 1):
                md += f"{i}. {alt}\n"

        if result.raw_response:
            md += "\n## Raw LLM Response\n<details>\n<summary>Click to expand raw response</summary>\n\n```\n" + result.raw_response + "\n```\n\n</details>\n"

        return md


def load_config(config_path: str = "config/config.json") -> dict:
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
