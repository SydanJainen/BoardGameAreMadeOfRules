import csv
import json
import logging
import re
import statistics
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

logger = logging.getLogger(__name__)



class MechanicsNormalizer:
    _instance: Optional['MechanicsNormalizer'] = None
    _mapping: Dict[str, Dict[str, any]] = None

    @classmethod
    def get_instance(cls) -> 'MechanicsNormalizer':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._load_mapping()

    def _load_mapping(self):
        mapping_path = Path("config/mechanics_mapping.json")

        if not mapping_path.exists():
            logger.warning(
                f"Mechanics mapping file not found at {mapping_path}. "
                "Normalization will be disabled (pass-through mode)."
            )
            self._mapping = {}
            return

        try:
            with open(mapping_path, encoding='utf-8') as f:
                data = json.load(f)
                self._mapping = data.get("mappings", {})

            logger.info(
                f"Loaded mechanics mapping with {len(self._mapping)} entries "
                f"from {mapping_path}"
            )

        except json.JSONDecodeError as e:
            logger.error(
                f"Invalid JSON in mechanics mapping file {mapping_path}: {e}. "
                "Normalization will be disabled."
            )
            self._mapping = {}
        except Exception as e:
            logger.error(
                f"Error loading mechanics mapping from {mapping_path}: {e}. "
                "Normalization will be disabled."
            )
            self._mapping = {}

    def normalize(self, mechanics: Optional[List[str]]) -> List[str]:
        if not mechanics:
            return []

        if not self._mapping:
            return list(set(mechanics))

        normalized = []
        mapped_count = 0

        for mech in mechanics:
            if not mech or not isinstance(mech, str):
                continue

            key = mech.lower().strip()

            if key in self._mapping:
                mapping_entry = self._mapping[key]
                bgg_mech = mapping_entry.get("bgg_mechanic")

                if bgg_mech:
                    normalized.append(bgg_mech)
                    mapped_count += 1
                else:
                    normalized.append(mech)
            else:
                normalized.append(mech)

        unique_normalized = []
        seen = set()
        for mech in normalized:
            key = mech.lower().strip()
            if key not in seen:
                seen.add(key)
                unique_normalized.append(mech)

        if mapped_count > 0:
            logger.debug(
                f"Normalized {mapped_count}/{len(mechanics)} mechanics "
                f"({len(mechanics) - len(unique_normalized)} duplicates removed)"
            )

        return unique_normalized



@dataclass
class ClassificationMetrics:
    precision: float
    recall: float
    f1_score: float
    support: int
    true_positives: int = 0
    false_positives: int = 0
    false_negatives: int = 0

    @classmethod
    def from_sets(cls, predicted: Set[str], actual: Set[str]) -> "ClassificationMetrics":
        if not predicted and not actual:
            return cls(1.0, 1.0, 1.0, 0, 0, 0, 0)

        normalizer = MechanicsNormalizer.get_instance()
        predicted_normalized = normalizer.normalize(list(predicted))

        predicted_norm = {p.lower().strip() for p in predicted_normalized if p}
        actual_norm = {a.lower().strip() for a in actual if a}

        true_positives = len(predicted_norm & actual_norm)
        false_positives = len(predicted_norm - actual_norm)
        false_negatives = len(actual_norm - predicted_norm)

        precision = true_positives / len(predicted_norm) if predicted_norm else 0.0
        recall = true_positives / len(actual_norm) if actual_norm else 0.0

        if precision + recall > 0:
            f1 = 2 * (precision * recall) / (precision + recall)
        else:
            f1 = 0.0

        return cls(
            precision=round(precision, 4),
            recall=round(recall, 4),
            f1_score=round(f1, 4),
            support=len(actual),
            true_positives=true_positives,
            false_positives=false_positives,
            false_negatives=false_negatives
        )

    def to_dict(self) -> Dict[str, float]:
        return {
            "precision": self.precision,
            "recall": self.recall,
            "f1_score": self.f1_score,
            "support": self.support,
            "true_positives": self.true_positives,
            "false_positives": self.false_positives,
            "false_negatives": self.false_negatives
        }


@dataclass
class BGGAccuracyMetrics:
    mechanics_f1: float
    mechanics_precision: float
    mechanics_recall: float
    complexity_error: float
    complexity_accuracy: float
    player_count_match: bool
    player_count_accuracy: float
    duration_error: float
    duration_error_pct: float
    overall_score: float

    @classmethod
    def calculate(
        cls,
        predicted_mechanics: Set[str],
        actual_mechanics: Set[str],
        predicted_complexity: float,
        actual_complexity: float,
        predicted_players: Tuple[int, int],
        actual_players: Tuple[int, int],
        predicted_duration: int,
        actual_duration: int,
        weights: Optional[Dict[str, float]] = None
    ) -> "BGGAccuracyMetrics":
        if weights is None:
            weights = {
                "mechanics": 0.4,
                "complexity": 0.2,
                "players": 0.2,
                "duration": 0.2
            }

        mech_metrics = ClassificationMetrics.from_sets(predicted_mechanics, actual_mechanics)
        mechanics_f1 = mech_metrics.f1_score
        mechanics_precision = mech_metrics.precision
        mechanics_recall = mech_metrics.recall

        complexity_error = abs(predicted_complexity - actual_complexity)
        complexity_accuracy = max(0.0, 1.0 - complexity_error / 5.0)

        player_match = (predicted_players == actual_players)
        player_accuracy = 1.0 if player_match else 0.0

        duration_error = abs(predicted_duration - actual_duration)
        if actual_duration > 0:
            duration_error_pct = duration_error / actual_duration
        else:
            duration_error_pct = 0.0 if predicted_duration == 0 else 1.0

        duration_accuracy = max(0.0, 1.0 - duration_error_pct)

        overall = (
            mechanics_f1 * weights["mechanics"] +
            complexity_accuracy * weights["complexity"] +
            player_accuracy * weights["players"] +
            duration_accuracy * weights["duration"]
        )

        return cls(
            mechanics_f1=round(mechanics_f1, 4),
            mechanics_precision=round(mechanics_precision, 4),
            mechanics_recall=round(mechanics_recall, 4),
            complexity_error=round(complexity_error, 2),
            complexity_accuracy=round(complexity_accuracy, 4),
            player_count_match=player_match,
            player_count_accuracy=player_accuracy,
            duration_error=round(duration_error, 1),
            duration_error_pct=round(duration_error_pct, 4),
            overall_score=round(overall, 4)
        )

    def to_dict(self) -> Dict[str, float]:
        return {
            "mechanics_f1": self.mechanics_f1,
            "mechanics_precision": self.mechanics_precision,
            "mechanics_recall": self.mechanics_recall,
            "complexity_error": self.complexity_error,
            "complexity_accuracy": self.complexity_accuracy,
            "player_count_match": self.player_count_match,
            "player_count_accuracy": self.player_count_accuracy,
            "duration_error": self.duration_error,
            "duration_error_pct": self.duration_error_pct,
            "overall_score": self.overall_score
        }


@dataclass
class InterModelAgreement:
    avg_jaccard: float
    min_jaccard: float
    max_jaccard: float
    agreement_matrix: Dict[str, Dict[str, float]]
    unanimous_items: Set[str]
    controversial_items: Set[str]

    @classmethod
    def calculate(
        cls,
        model_outputs: Dict[str, Set[str]]
    ) -> "InterModelAgreement":
        models = list(model_outputs.keys())
        n = len(models)

        if n < 2:
            return cls(
                avg_jaccard=1.0,
                min_jaccard=1.0,
                max_jaccard=1.0,
                agreement_matrix={},
                unanimous_items=set(model_outputs.get(models[0], set())) if models else set(),
                controversial_items=set()
            )

        normalized_outputs = {
            model: {item.lower().strip() for item in items if item}
            for model, items in model_outputs.items()
        }
        agreement_matrix = {}
        jaccard_scores = []

        for i, m1 in enumerate(models):
            agreement_matrix[m1] = {}
            for j, m2 in enumerate(models):
                if i == j:
                    agreement_matrix[m1][m2] = 1.0
                else:
                    set1 = normalized_outputs[m1]
                    set2 = normalized_outputs[m2]

                    if not set1 and not set2:
                        jacc = 1.0
                    elif not set1 or not set2:
                        jacc = 0.0
                    else:
                        intersection = len(set1 & set2)
                        union = len(set1 | set2)
                        jacc = intersection / union if union > 0 else 0.0

                    agreement_matrix[m1][m2] = round(jacc, 4)
                    if i < j:
                        jaccard_scores.append(jacc)

        avg_jaccard = statistics.mean(jaccard_scores) if jaccard_scores else 1.0
        min_jaccard = min(jaccard_scores) if jaccard_scores else 1.0
        max_jaccard = max(jaccard_scores) if jaccard_scores else 1.0

        all_items = set()
        for items in normalized_outputs.values():
            all_items.update(items)

        unanimous_items = set()
        controversial_items = set()

        for item in all_items:
            models_with_item = sum(1 for items in normalized_outputs.values() if item in items)
            if models_with_item == n:
                unanimous_items.add(item)
            elif models_with_item < n and models_with_item > 0:
                controversial_items.add(item)

        return cls(
            avg_jaccard=round(avg_jaccard, 4),
            min_jaccard=round(min_jaccard, 4),
            max_jaccard=round(max_jaccard, 4),
            agreement_matrix=agreement_matrix,
            unanimous_items=unanimous_items,
            controversial_items=controversial_items
        )

    def to_dict(self) -> Dict:
        return {
            "avg_jaccard": self.avg_jaccard,
            "min_jaccard": self.min_jaccard,
            "max_jaccard": self.max_jaccard,
            "agreement_matrix": self.agreement_matrix,
            "unanimous_items": list(self.unanimous_items),
            "controversial_items": list(self.controversial_items)
        }


def evaluate_explanation_quality(
    explanation: str,
    audience: str,
    rulebook_text: str = ""
) -> Dict[str, float]:
    if not explanation:
        return {
            "coverage": 0.0,
            "length_ratio": 0.0,
            "readability_score": 0.0,
            "word_count": 0,
            "avg_sentence_length": 0.0
        }

    key_terms = [
        "setup", "turn", "win", "player", "card", "board",
        "piece", "score", "round", "phase", "action", "draw",
        "play", "move", "rule", "game"
    ]
    explanation_lower = explanation.lower()
    coverage = sum(1 for term in key_terms if term in explanation_lower) / len(key_terms)

    words = explanation.split()
    word_count = len(words)

    target_lengths = {"child": 400, "adult": 800, "expert": 1200}
    target = target_lengths.get(audience, 800)

    if word_count > 0 and target > 0:
        ratio = word_count / target
        if ratio > 1:
            length_ratio = 1 / ratio
        else:
            length_ratio = ratio
    else:
        length_ratio = 0.0

    sentences = [s.strip() for s in explanation.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    if sentences:
        sentence_lengths = [len(s.split()) for s in sentences]
        avg_sentence_length = statistics.mean(sentence_lengths)
    else:
        avg_sentence_length = 0.0

    target_sentence = {"child": 8, "adult": 15, "expert": 20}
    target_sent = target_sentence.get(audience, 15)

    if avg_sentence_length > 0 and target_sent > 0:
        sent_ratio = avg_sentence_length / target_sent
        if sent_ratio > 1:
            readability = max(0, 1 - (sent_ratio - 1) * 0.5)
        else:
            readability = max(0, 1 - (1 - sent_ratio) * 0.3)
    else:
        readability = 0.0

    return {
        "coverage": round(coverage, 4),
        "length_ratio": round(length_ratio, 4),
        "readability_score": round(readability, 4),
        "word_count": word_count,
        "avg_sentence_length": round(avg_sentence_length, 2)
    }


def calculate_model_ranking(
    results: List[Dict[str, float]],
    metric_weights: Optional[Dict[str, float]] = None
) -> List[Tuple[str, float]]:
    if not results:
        return []
    metrics = [k for k in results[0].keys() if k != 'model']

    if metric_weights is None:
        metric_weights = {m: 1.0 / len(metrics) for m in metrics}

    rankings = []
    for r in results:
        model = r.get('model', 'unknown')
        score = sum(r.get(m, 0) * metric_weights.get(m, 0) for m in metrics)
        rankings.append((model, round(score, 4)))

    return sorted(rankings, key=lambda x: x[1], reverse=True)


@dataclass
class ExperimentResults:
    game: str
    model: str
    model_alias: str
    audience: str
    task: str
    execution_time: float
    tokens: int = 0
    metrics: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


class ResultsAggregator:

    def __init__(self):
        self.results: List[ExperimentResults] = []

    def add_result(self, result: ExperimentResults):
        self.results.append(result)

    def load_from_directory(
        self,
        results_dir: str,
        task: str = "explain",
        pattern: str = "*.md"
    ) -> int:

        try:
            import yaml
        except ImportError:
            print("Warning: pyyaml not installed, using regex parsing")
            yaml = None

        path = Path(results_dir)
        if not path.exists():
            return 0

        loaded = 0
        for file in path.glob(pattern):
            try:
                content = file.read_text(encoding='utf-8')

                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        if yaml:
                            metadata = yaml.safe_load(parts[1])
                        else:
                            metadata = self._parse_yaml_simple(parts[1])

                        if metadata:
                            name_parts = file.stem.split('_')

                            if len(name_parts) >= 3:
                                game = name_parts[0]
                                audience = name_parts[1]
                                model_alias = name_parts[-1]
                            elif len(name_parts) == 2:
                                game = name_parts[0]
                                audience = "unknown"
                                model_alias = name_parts[1]
                            else:
                                game = file.stem
                                audience = "unknown"
                                model_alias = metadata.get('model_alias', 'unknown')

                            result = ExperimentResults(
                                game=game,
                                model=metadata.get('model', 'unknown'),
                                model_alias=metadata.get('model_alias', model_alias),
                                audience=audience,
                                task=task,
                                execution_time=metadata.get('execution_time_seconds', 0),
                                tokens=metadata.get('tokens', 0),
                                metadata=metadata
                            )
                            self.results.append(result)
                            loaded += 1

            except Exception as e:
                print(f"Warning: Could not parse {file}: {e}")
                continue

        return loaded

    def _parse_yaml_simple(self, yaml_str: str) -> Dict:
        result = {}
        for line in yaml_str.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip("'\"")

                try:
                    if '.' in value:
                        result[key] = float(value)
                    else:
                        result[key] = int(value)
                except ValueError:
                    result[key] = value

        return result

    def get_summary_by_model(self) -> Dict[str, Dict]:
        summary = {}
        for r in self.results:
            model = r.model_alias or r.model
            if model not in summary:
                summary[model] = {
                    'count': 0,
                    'total_time': 0.0,
                    'total_tokens': 0,
                    'games': set(),
                    'audiences': set()
                }
            summary[model]['count'] += 1
            summary[model]['total_time'] += r.execution_time
            summary[model]['total_tokens'] += r.tokens
            summary[model]['games'].add(r.game)
            summary[model]['audiences'].add(r.audience)

        for model in summary:
            count = summary[model]['count']
            if count > 0:
                summary[model]['avg_time'] = round(summary[model]['total_time'] / count, 2)
                summary[model]['avg_tokens'] = round(summary[model]['total_tokens'] / count, 1)
            else:
                summary[model]['avg_time'] = 0
                summary[model]['avg_tokens'] = 0

            summary[model]['games'] = sorted(list(summary[model]['games']))
            summary[model]['audiences'] = sorted(list(summary[model]['audiences']))

        return summary

    def get_summary_by_game(self) -> Dict[str, Dict]:
        summary = {}
        for r in self.results:
            game = r.game
            if game not in summary:
                summary[game] = {
                    'count': 0,
                    'models': set(),
                    'avg_time': 0.0,
                    'total_time': 0.0
                }
            summary[game]['count'] += 1
            summary[game]['models'].add(r.model_alias or r.model)
            summary[game]['total_time'] += r.execution_time

        for game in summary:
            count = summary[game]['count']
            if count > 0:
                summary[game]['avg_time'] = round(summary[game]['total_time'] / count, 2)
            summary[game]['models'] = sorted(list(summary[game]['models']))

        return summary

    def get_summary_by_audience(self) -> Dict[str, Dict]:
        summary = {}
        for r in self.results:
            aud = r.audience
            if aud not in summary:
                summary[aud] = {
                    'count': 0,
                    'avg_time': 0.0,
                    'avg_tokens': 0.0,
                    'total_time': 0.0,
                    'total_tokens': 0
                }
            summary[aud]['count'] += 1
            summary[aud]['total_time'] += r.execution_time
            summary[aud]['total_tokens'] += r.tokens

        for aud in summary:
            count = summary[aud]['count']
            if count > 0:
                summary[aud]['avg_time'] = round(summary[aud]['total_time'] / count, 2)
                summary[aud]['avg_tokens'] = round(summary[aud]['total_tokens'] / count, 1)

        return summary

    def get_cross_table(self, row_key: str = "model", col_key: str = "game", value_key: str = "execution_time") -> Dict:
        rows = set()
        cols = set()
        values = {}

        for r in self.results:
            row = getattr(r, row_key, None) or r.model_alias
            col = getattr(r, col_key, None) or r.game
            val = getattr(r, value_key, 0)

            rows.add(row)
            cols.add(col)

            if row not in values:
                values[row] = {}
            if col not in values[row]:
                values[row][col] = []
            values[row][col].append(val)

        for row in values:
            for col in values[row]:
                vals = values[row][col]
                values[row][col] = round(sum(vals) / len(vals), 2) if vals else 0

        return {
            "rows": sorted(list(rows)),
            "cols": sorted(list(cols)),
            "values": values
        }

    def filter(
        self,
        model: Optional[str] = None,
        game: Optional[str] = None,
        audience: Optional[str] = None,
        task: Optional[str] = None
    ) -> "ResultsAggregator":
        filtered = ResultsAggregator()
        for r in self.results:
            if model and r.model_alias != model and r.model != model:
                continue
            if game and r.game != game:
                continue
            if audience and r.audience != audience:
                continue
            if task and r.task != task:
                continue
            filtered.add_result(r)
        return filtered

    def export_csv(self, output_path: str):
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'game', 'model', 'model_alias', 'audience', 'task',
                'execution_time', 'tokens'
            ])
            writer.writeheader()
            for r in self.results:
                writer.writerow({
                    'game': r.game,
                    'model': r.model,
                    'model_alias': r.model_alias,
                    'audience': r.audience,
                    'task': r.task,
                    'execution_time': r.execution_time,
                    'tokens': r.tokens
                })

    def export_json(self, output_path: str):
        data = {
            'total_experiments': len(self.results),
            'results': [
                {
                    'game': r.game,
                    'model': r.model,
                    'model_alias': r.model_alias,
                    'audience': r.audience,
                    'task': r.task,
                    'execution_time': r.execution_time,
                    'tokens': r.tokens,
                    'metrics': r.metrics
                }
                for r in self.results
            ],
            'summary_by_model': self.get_summary_by_model(),
            'summary_by_game': self.get_summary_by_game(),
            'summary_by_audience': self.get_summary_by_audience()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, default=str)

    def print_summary(self):
        print(f"\n{'='*60}")
        print(f"EXPERIMENT SUMMARY")
        print(f"{'='*60}")
        print(f"Total experiments: {len(self.results)}")

        print(f"\n--- By Model ---")
        for model, stats in sorted(self.get_summary_by_model().items()):
            print(f"  {model}: {stats['count']} runs, avg {stats['avg_time']}s, {stats['avg_tokens']} tokens")

        print(f"\n--- By Game ---")
        for game, stats in sorted(self.get_summary_by_game().items()):
            print(f"  {game}: {stats['count']} runs, avg {stats['avg_time']}s")

        print(f"\n--- By Audience ---")
        for aud, stats in sorted(self.get_summary_by_audience().items()):
            print(f"  {aud}: {stats['count']} runs, avg {stats['avg_time']}s, {stats['avg_tokens']} tokens")

        print(f"{'='*60}\n")
