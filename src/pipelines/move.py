import re
from typing import Any, Dict, List

from src.core.models import MoveRecommendation, ProcessedContent, RawContent
from .base import AbstractPipeline


class MovePipeline(AbstractPipeline):

    def load_data(self) -> RawContent:
        return self.data_adapter.load()

    def extract_content(self, raw_content: RawContent) -> str:
        return raw_content.text

    def format_result(
        self, processed: ProcessedContent, raw_content: RawContent, **kwargs
    ) -> MoveRecommendation:
        game_state = kwargs.get("game_state", kwargs.get("state", ""))
        parsed = self._parse_move_recommendation(processed.text)

        return MoveRecommendation(
            current_state=game_state,
            recommended_move=parsed["move"],
            reasoning=parsed["reasoning"],
            alternative_moves=parsed["alternatives"],
            execution_metadata=processed.execution_metadata,
            raw_response=processed.raw_response,
        )

    def _parse_move_recommendation(self, response: str) -> Dict[str, Any]:
        result: Dict[str, Any] = {"move": "", "reasoning": "", "alternatives": []}

        current_section = None
        reasoning_lines: List[str] = []

        lines = response.split("\n")
        for line in lines:
            line_stripped = line.strip()
            line_upper = line_stripped.upper()

            if "RECOMMENDED MOVE:" in line_upper:
                current_section = "move"
                if ":" in line_stripped:
                    move_part = line_stripped.split(":", 1)[1].strip()
                    if move_part:
                        result["move"] = move_part
            elif "REASONING:" in line_upper:
                current_section = "reasoning"
            elif "ALTERNATIVE MOVES:" in line_upper:
                current_section = "alternatives"
            else:
                if current_section == "move" and line_stripped:
                    if not result["move"]:
                        result["move"] = line_stripped
                elif current_section == "reasoning" and line_stripped:
                    reasoning_lines.append(line_stripped)
                elif current_section == "alternatives":
                    match = re.match(r"^\d+\.\s*(.+)$", line_stripped)
                    if match:
                        result["alternatives"].append(match.group(1))

        result["reasoning"] = " ".join(reasoning_lines)

        return result
