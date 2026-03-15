class MovePrompt:
    def build_prompt(self, content: str, game_state: str = "", **kwargs) -> str:
        if not game_state:
            game_state = kwargs.get("state", "No game state provided")

        return f"""You are a board game expert analysing a game in progress.

GAME RULES:
{content}

CURRENT GAME STATE:
{game_state}

TASK:
Based on the rules and current game state, provide:
1. An analysis of the current situation
2. A recommended move for the current player
3. The reasoning behind this recommendation
4. Alternative moves to consider

Be strategic and explain your thinking clearly.

OUTPUT FORMAT:
SITUATION ANALYSIS:
[Analysis of current state]

RECOMMENDED MOVE:
[Specific move recommendation]

REASONING:
[Why this is the best move]

ALTERNATIVE MOVES:
1. [Alternative option 1]
2. [Alternative option 2]
3. [Alternative option 3]

YOUR RECOMMENDATION:"""
