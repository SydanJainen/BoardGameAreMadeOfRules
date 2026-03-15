class InventPrompt:
    def build_prompt(
        self,
        content: str,
        theme: str = "",
        mechanics: str = "",
        format_instructions: str = "",
        custom_prompt: str = "",
        prompt_file: str = "",
        **kwargs,
    ) -> str:
        # Priority: prompt_file > custom_prompt > standard
        if prompt_file:
            prompt_body = self._load_prompt_file(prompt_file)
        elif custom_prompt:
            prompt_body = custom_prompt
        else:
            prompt_body = self._build_standard_prompt(content, theme, mechanics)

        return f"""You are an expert board game designer writing a complete design document. Your document must be detailed enough that a group of players could play the game using ONLY what you write — no guessing, no ambiguity.

{prompt_body}

YOUR COMPLETE GAME DESIGN:"""

    def _load_prompt_file(self, path: str) -> str:
        from pathlib import Path

        file_path = Path(path)
        if file_path.exists():
            return file_path.read_text(encoding="utf-8")

        project_root = Path(__file__).resolve().parent.parent.parent
        project_path = project_root / path
        if project_path.exists():
            return project_path.read_text(encoding="utf-8")

        raise FileNotFoundError(
            f"Prompt file not found: '{path}'. "
            f"Tried: '{file_path.resolve()}' and '{project_path.resolve()}'"
        )

    def _build_standard_prompt(self, content: str, theme: str, mechanics: str) -> str:
        theme_section = f"\nTHEME DIRECTION: {theme}" if theme else ""
        mechanics_section = f"\nPREFERRED MECHANICS: {mechanics}" if mechanics else ""

        return f"""CONCEPT:
{content}
{theme_section}
{mechanics_section}

Write the following sections using the EXACT headers shown. Every section is mandatory.

GAME NAME: A creative, evocative name.

THEME: The game's world and narrative premise. What do players represent? What drives the conflict? Why is this setting compelling? Write 3-5 sentences that make the theme inseparable from the gameplay.

MECHANICS: List 3-5 core mechanics. For EACH mechanic write 2-3 sentences explaining HOW it works in THIS game and what decisions it creates for players. Do not just list names.

COMPONENTS: List every physical component with exact quantities and descriptions. Example format: "48 Resource Cards (12 per type: Wood, Stone, Iron, Crystal)", "1 Game Board (hex grid, 37 tiles)".

PLAYERS: Player count range.
DURATION: Estimated play time.

SETUP:
Write a numbered step-by-step procedure. A player reading this must be able to set up the game with zero ambiguity. Cover: board assembly, deck preparation, initial resource distribution, starting positions, first player selection.

RULES:
This is the most important section. Write a COMPLETE rulebook covering everything below. Players must be able to play the game using ONLY this text.

A) TURN STRUCTURE: Describe the exact sequence of phases in each turn. For each phase state what happens and whether it is mandatory or optional.

B) ACTION CATALOG: For EVERY action a player can take, write a dedicated paragraph covering:
   - Name of the action
   - When it can be performed (which phase, any prerequisites)
   - Cost (resources, action points, cards to discard, etc.)
   - Step-by-step resolution (what happens mechanically)
   - Restrictions and limits (once per turn? requires adjacency? etc.)
   - Brief example: "Example: Alice spends 2 Wood and 1 Stone to build a Watchtower on hex B3. She places a Watchtower token and draws 1 Patrol card."
   Do NOT skip any action. Do NOT write "etc." or "and so on". Every single action must be fully described.

C) PLAYER INTERACTION: How do players affect each other? Cover: trading rules (if any), combat/conflict resolution (exact procedure with step-by-step), blocking and area control, alliances or negotiations. If players do NOT interact directly, explain what indirect competition exists.

D) RESOURCE FLOW: How are resources gained, spent, and lost? What are the limits (hand size, storage)? When do resources refresh? Is there a market or economy?

E) SPECIAL RULES: Card effects (describe the card types and what each type does), environmental effects, event resolution, any situational rules that do not fit above.

F) END GAME: Exactly when and how the game ends. ALL victory conditions with exact scoring. Tiebreaker rules.

G) EXAMPLE ROUND: Write one full example round with 2-3 players. Show each player's turn step-by-step with specific decisions, costs paid, and outcomes. This should demonstrate the game flow and at least 3 different actions.

Write the rules section at length — this should be the longest part of your document by far."""

    def build_retry_prompt(
        self,
        content: str,
        original_response: str,
        missing_fields: str,
        theme: str = "",
        mechanics: str = "",
        format_instructions: str = "",
        **kwargs,
    ) -> str:
        theme_section = f"THEME: {theme}" if theme else ""
        mechanics_section = f"PREFERRED MECHANICS: {mechanics}" if mechanics else ""

        return f"""Your previous game design was incomplete. Fix the issues below and provide a COMPLETE, DETAILED design.

ISSUES FOUND:
{missing_fields}

ORIGINAL CONCEPT:
{content}

{theme_section}
{mechanics_section}

PREVIOUS RESPONSE (INCOMPLETE):
{original_response}

FIX REQUIREMENTS:
- Game Name: Must be unique and creative (not "Untitled Game" or similar)
- Theme: Must be a rich description (minimum 3 sentences)
- Mechanics: Must list at least 3 distinct mechanics with explanations of how each works
- Components: Must list at least 5 specific items with quantities
- Rules: Must include turn structure, action catalog, player interaction, and example round

PROVIDE THE COMPLETE, DETAILED GAME DESIGN:"""

