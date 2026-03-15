import logging
from typing import Any, Optional, Tuple

from src.core.models import InventResult, ProcessedContent, RawContent
from src.core.utils import validate_board_game
from .base import AbstractPipeline

logger = logging.getLogger(__name__)


class InventPipeline(AbstractPipeline):

    def __init__(
        self,
        data_adapter,
        llm_client,
        prompt_strategy,
        preprocessor,
        response_parser=None,
    ):
        super().__init__(
            data_adapter=data_adapter,
            llm_client=llm_client,
            prompt_strategy=prompt_strategy,
            preprocessor=preprocessor,
        )
        self.response_parser = response_parser

    def load_data(self) -> RawContent:
        return self.data_adapter.load()

    def extract_content(self, raw_content: RawContent) -> str:
        return raw_content.text

    def process_with_llm(self, text: str, **kwargs):
        if self.response_parser:
            kwargs["format_instructions"] = (
                self.response_parser.get_format_instructions()
            )
        return super().process_with_llm(text, **kwargs)

    def format_result(
        self,
        processed: ProcessedContent,
        raw_content: RawContent,
        **kwargs,
    ) -> InventResult:
        if self.response_parser:
            parsed = self.response_parser.parse(processed.text, InventResult)
        else:
            parsed = self._parse_game_design_legacy(processed.text)

        is_valid, error_message = validate_board_game(parsed)

        retry_metadata = {
            "retry_triggered": False,
            "retry_count": 0,
            "retry_reason": "",
            "final_validation_passed": is_valid,
        }

        if not is_valid and self.response_parser:
            logger.info(f"Validation failed: {error_message}. Triggering retry.")
            retry_metadata["retry_triggered"] = True
            retry_metadata["retry_reason"] = error_message

            parsed_retry, is_valid_retry = self._retry_with_enhanced_prompt(
                raw_content=raw_content,
                original_response=processed.text,
                missing_fields=error_message,
                theme=kwargs.get("theme", ""),
                mechanics=kwargs.get("mechanics", ""),
            )

            if parsed_retry:
                retry_metadata["retry_count"] = 1
                retry_metadata["final_validation_passed"] = is_valid_retry
                parsed = parsed_retry
                if is_valid_retry:
                    logger.info("Retry succeeded: validation passed.")
                else:
                    logger.warning(
                        "Retry completed but validation still failed. Accepting result anyway."
                    )
            else:
                logger.warning(
                    "Retry failed: could not parse retry response. Using original."
                )

        if processed.execution_metadata:
            processed.execution_metadata.additional_params["retry_info"] = (
                retry_metadata
            )

        return InventResult(
            game_name=parsed.get("game_name") or parsed.get("name", "Untitled Game"),
            theme=parsed.get("theme", ""),
            mechanics=parsed.get("mechanics", []),
            rules=parsed.get("rules", ""),
            components=parsed.get("components", []),
            player_count=parsed.get("player_count") or parsed.get("players", "2-4"),
            duration=parsed.get("duration", "60 minutes"),
            execution_metadata=processed.execution_metadata,
            raw_response=processed.raw_response,
        )

    def _retry_with_enhanced_prompt(
        self,
        raw_content: RawContent,
        original_response: str,
        missing_fields: str,
        theme: str = "",
        mechanics: str = "",
    ) -> Tuple[Optional[dict], bool]:
        try:
            retry_prompt = self.prompt_strategy.build_retry_prompt(
                content=raw_content.text,
                original_response=original_response,
                missing_fields=missing_fields,
                theme=theme,
                mechanics=mechanics,
                format_instructions=(
                    self.response_parser.get_format_instructions()
                    if self.response_parser
                    else ""
                ),
            )

            retry_response = self.llm_client.generate(retry_prompt)

            if self.response_parser:
                parsed_retry = self.response_parser.parse(retry_response, InventResult)
            else:
                parsed_retry = self._parse_game_design_legacy(retry_response)

            is_valid_retry, _ = validate_board_game(parsed_retry)

            return parsed_retry, is_valid_retry

        except Exception as e:
            logger.error(f"Retry failed with exception: {e}")
            return None, False

    def _parse_game_design_legacy(self, response: str) -> dict:
        result = {
            "name": "Untitled Game",
            "theme": "",
            "mechanics": [],
            "components": [],
            "players": "2-4",
            "duration": "60 minutes",
            "rules": "",
        }

        current_section = None
        rules_lines = []

        lines = response.split("\n")
        for line in lines:
            line_stripped = line.strip()
            line_upper = line_stripped.upper()

            if line_upper.startswith("GAME NAME:"):
                result["name"] = line_stripped.split(":", 1)[1].strip()
            elif line_upper.startswith("THEME:"):
                result["theme"] = line_stripped.split(":", 1)[1].strip()
            elif line_upper.startswith("MECHANICS:"):
                mech_str = line_stripped.split(":", 1)[1].strip()
                result["mechanics"] = [m.strip() for m in mech_str.split(",")]
            elif line_upper.startswith("COMPONENTS:"):
                comp_str = line_stripped.split(":", 1)[1].strip()
                result["components"] = [
                    c.strip() for c in comp_str.split(",") if c.strip()
                ]
            elif line_upper.startswith("PLAYERS:"):
                result["players"] = line_stripped.split(":", 1)[1].strip()
            elif line_upper.startswith("DURATION:"):
                result["duration"] = line_stripped.split(":", 1)[1].strip()
            elif any(
                line_upper.startswith(h.rstrip(":"))
                or line_upper.startswith("## " + h.rstrip(":"))
                for h in [
                    "SETUP:",
                    "GAMEPLAY:",
                    "WINNING CONDITION:",
                    "RULES:",
                    "WINNING:",
                ]
            ):
                current_section = "rules"
                rules_lines.append(line_stripped)
            elif current_section == "rules":
                rules_lines.append(line)

        result["rules"] = "\n".join(rules_lines).strip()

        if not result["rules"]:
            result["rules"] = response.strip()

        return result
