class AnalysePrompt:
    def build_prompt(self, content: str, **kwargs) -> str:
        return f"""You are a board game expert analysing game mechanics and properties.

RULEBOOK:
{content}

TASK:
Analyse this game and provide the following information in a structured format:

1. MECHANICS: List the main game mechanics (e.g., worker placement, deck building, area control, resource management, dice rolling, card drafting, tile placement, set collection, hand management, trading, negotiation, pattern building)

2. COMPLEXITY: Rate the game complexity on a scale of 1.0 to 5.0, where:
   - 1.0 = Very simple (children's games)
   - 2.0 = Simple (family games)
   - 3.0 = Medium (gateway games)
   - 4.0 = Complex (hobby games)
   - 5.0 = Very complex (expert games)

3. PLAYER COUNT: Minimum and maximum number of players.

4. DURATION: Estimated playing time in minutes.

OUTPUT FORMAT (use exactly this format):
MECHANICS: [comma-separated list]
COMPLEXITY: [number between 1.0 and 5.0]
PLAYERS: [min]-[max]
DURATION: [minutes]

YOUR ANALYSIS:"""
