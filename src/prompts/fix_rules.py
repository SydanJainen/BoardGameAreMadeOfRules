class FixRulesPrompt:
    def build_prompt(self, content: str, **kwargs) -> str:
        return f"""You are a board game expert reviewing game rules for clarity and completeness.

RULEBOOK:
{content}

TASK:
Carefully review these rules and identify any issues, including:
- Missing rules or incomplete explanations
- Ambiguous or unclear instructions
- Logical inconsistencies or contradictions
- Missing edge cases or conflict resolution rules
- Unclear winning conditions
- Undefined terms or components

For each issue found, suggest a specific correction or addition.

OUTPUT FORMAT:
ISSUES IDENTIFIED:
1. [Description of issue]
2. [Description of issue]
...

SUGGESTED FIXES:
1. [Specific correction or addition]
2. [Specific correction or addition]
...

CORRECTED RULES:
[Provide a corrected version of the problematic sections]

YOUR ANALYSIS:"""
