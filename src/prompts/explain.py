from src.core.models import Audience


class ExplainPrompt:
    def build_prompt(self, content: str, audience: Audience = Audience.ADULT, **kwargs) -> str:
        audience_instructions = {
            Audience.CHILD: """Explain the rules in a way that a 10-year-old child can understand.
Use simple words, short sentences, and fun examples.
Avoid complex terminology and focus on the most important rules.""",
            Audience.ADULT: """Explain the rules clearly and concisely for adult players.
Use standard board game terminology and provide a complete overview.
Focus on setup, gameplay, and winning conditions.""",
            Audience.EXPERT: """Provide a detailed expert-level analysis of the rules.
Include strategic considerations, edge cases, and rule interactions.
Use precise terminology and assume deep board game knowledge.""",
        }

        instruction = audience_instructions.get(audience, audience_instructions[Audience.ADULT])

        return f"""You are a board game expert explaining game rules.

{instruction}

RULEBOOK:
{content}

TASK:
Explain the rules of this game clearly and accurately for the {audience.value} audience.

YOUR EXPLANATION:"""
