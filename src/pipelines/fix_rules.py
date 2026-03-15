import re
from typing import Any, List, Tuple

from src.core.models import FixRulesResult, ProcessedContent, RawContent
from .base import AbstractPipeline


class FixRulesPipeline(AbstractPipeline):

    def load_data(self) -> RawContent:
        return self.data_adapter.load()

    def extract_content(self, raw_content: RawContent) -> str:
        return raw_content.text

    def format_result(
        self, processed: ProcessedContent, raw_content: RawContent, **kwargs
    ) -> FixRulesResult:
        issues, fixes, corrected = self._parse_fix_rules_response(processed.text)

        return FixRulesResult(
            identified_issues=issues,
            suggested_fixes=fixes,
            corrected_rules=corrected,
            execution_metadata=processed.execution_metadata,
            raw_response=processed.raw_response,
        )

    def _parse_fix_rules_response(self, response: str) -> Tuple[List[str], List[str], str]:
        issues = []
        fixes = []
        corrected = ""

        current_section = None
        corrected_lines = []

        lines = response.split("\n")
        for line in lines:
            line_upper = line.strip().upper()

            if "ISSUES IDENTIFIED:" in line_upper:
                current_section = "issues"
                continue
            elif "SUGGESTED FIXES:" in line_upper:
                current_section = "fixes"
                continue
            elif "CORRECTED RULES:" in line_upper:
                current_section = "corrected"
                continue

            if current_section == "issues":
                match = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if match:
                    issues.append(match.group(1))

            elif current_section == "fixes":
                match = re.match(r"^\d+\.\s*(.+)$", line.strip())
                if match:
                    fixes.append(match.group(1))

            elif current_section == "corrected":
                corrected_lines.append(line)

        corrected = "\n".join(corrected_lines).strip()

        return issues, fixes, corrected
