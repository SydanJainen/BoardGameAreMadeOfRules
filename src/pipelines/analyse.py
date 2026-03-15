import re
from typing import Any, List, Tuple

from src.core.models import AnalysisResult, ProcessedContent, RawContent
from .base import AbstractPipeline
from src.evaluation import MechanicsNormalizer


class AnalysePipeline(AbstractPipeline):

    def __init__(self, *args, bgg_adapter=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.bgg_adapter = bgg_adapter

    def execute(self, **kwargs):
        if self.data_adapter is None:
            if not self.bgg_adapter:
                raise ValueError("No data source available: neither file nor BGG adapter provided")

            bgg_data = self.bgg_adapter.load()
            return AnalysisResult(
                mechanics=bgg_data.metadata.get("mechanics", []),
                complexity=bgg_data.metadata.get("complexity", 0.0),
                min_players=bgg_data.metadata.get("min_players", 0),
                max_players=bgg_data.metadata.get("max_players", 0),
                duration_min=bgg_data.metadata.get("duration", 0),
                bgg_mechanics=bgg_data.metadata.get("mechanics", []),
                bgg_complexity=bgg_data.metadata.get("complexity", 0.0),
                bgg_players=f"{bgg_data.metadata.get('min_players', 0)}-{bgg_data.metadata.get('max_players', 0)}",
                bgg_duration=bgg_data.metadata.get("duration", 0),
                mechanics_similarity=None,
                complexity_error=None,
                overall_score=None,
            )

        return super().execute(**kwargs)

    def load_data(self) -> RawContent:
        if self.data_adapter is None:
            return None
        return self.data_adapter.load()

    def extract_content(self, raw_content: RawContent) -> str:
        return raw_content.text

    def format_result(
        self, processed: ProcessedContent, raw_content: RawContent, **kwargs
    ) -> AnalysisResult:
        mechanics, complexity, min_players, max_players, duration = self._parse_analysis(
            processed.text
        )

        result = AnalysisResult(
            mechanics=mechanics,
            complexity=complexity,
            min_players=min_players,
            max_players=max_players,
            duration_min=duration,
            execution_metadata=processed.execution_metadata,
            raw_response=processed.raw_response,
        )

        if self.bgg_adapter:
            bgg_data = self.bgg_adapter.load()
            result.bgg_mechanics = bgg_data.metadata.get("mechanics", [])
            result.bgg_complexity = bgg_data.metadata.get("complexity", 0.0)
            result.bgg_players = f"{bgg_data.metadata.get('min_players', 0)}-{bgg_data.metadata.get('max_players', 0)}"
            result.bgg_duration = bgg_data.metadata.get("duration", 0)

            normalizer = MechanicsNormalizer.get_instance()
            mechanics_normalized = normalizer.normalize(mechanics)

            result.mechanics_similarity = self._calculate_jaccard_similarity(
                set(mechanics_normalized), set(result.bgg_mechanics)
            )
            result.complexity_error = abs(complexity - result.bgg_complexity)

            result.overall_score = (
                0.5 * result.mechanics_similarity
                + 0.5 * (1.0 - result.complexity_error / 5.0)
            )

        return result

    def _parse_analysis(self, response: str) -> Tuple[List[str], float, int, int, int]:
        mechanics = []
        complexity = 2.5
        min_players = 2
        max_players = 4
        duration = 60

        lines = response.split("\n")
        for line in lines:
            line = line.strip()

            if line.startswith("MECHANICS:"):
                mech_str = line.split(":", 1)[1].strip()
                mechanics = [m.strip() for m in mech_str.split(",")]

            elif line.startswith("COMPLEXITY:"):
                try:
                    comp_str = line.split(":", 1)[1].strip()
                    complexity = float(re.findall(r"\d+\.?\d*", comp_str)[0])
                except (ValueError, IndexError):
                    complexity = 2.5

            elif line.startswith("PLAYERS:"):
                try:
                    players_str = line.split(":", 1)[1].strip()
                    match = re.search(r"(\d+)-(\d+)", players_str)
                    if match:
                        min_players = int(match.group(1))
                        max_players = int(match.group(2))
                except (ValueError, AttributeError):
                    pass

            elif line.startswith("DURATION:"):
                try:
                    duration_str = line.split(":", 1)[1].strip()
                    duration = int(re.findall(r"\d+", duration_str)[0])
                except (ValueError, IndexError):
                    duration = 60

        return mechanics, complexity, min_players, max_players, duration

    def _calculate_jaccard_similarity(self, set1: set, set2: set) -> float:
        if not set1 and not set2:
            return 1.0
        if not set1 or not set2:
            return 0.0

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0
