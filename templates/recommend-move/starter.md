---
command: recommend-move
version: "1.0"

metadata:
  name: "Recommend Move Template"
  description: "Suggest optimal moves given current game state"
  # author: "Your name"

context:
  # Optional: Provide game context
  # player_perspective: "Red"  # Which player to advise
  # game_phase: "Mid-game (Round 5 of 10)"  # Early/mid/late game
  # player_goals:  # What the player wants to achieve
  #   - "Build Longest Road"
  #   - "Reach 10 victory points"
  # game_history:  # Previous moves for context
  #   - "Turn 1-3: Focused on wood and brick"
  #   - "Turn 4: Opponent built settlement on key hex"

parameters:
  # Optional: Strategy preferences
  # strategy_style: balanced  # Options: aggressive, defensive, balanced
  # alternatives_count: 3  # How many options to suggest
  # explanation_detail: detailed  # Options: brief, moderate, detailed

  # Optional: Output settings
  format: markdown  # Options: markdown, json
  # output_file: "results/move-recommendation.md"  # Uncomment to save to file

content:
  # Option 1: Reference a rules file
  rules_file: "path/to/rulebook.pdf"

  # Option 2: Paste rules inline (remove rules_file if using this)
  # rules: |
  #   # Brief rules summary

  # Required: Current game state
  game_state: |
    Describe the current game state here.

    Example structure:

    ## My Position (Player Red)
    - Victory Points: 7
    - Resources: 2 wood, 1 brick, 3 ore, 1 wheat
    - Settlements: 2
    - Cities: 1
    - Special: Longest Road (5 segments)

    ## Opponents
    - Blue: 8 VP (threatening to win)
    - Green: 6 VP
    - Yellow: 5 VP

    ## Board State
    - Wheat is scarce
    - 2 good settlement spots remain
    - Robber on sheep hex

---

# Strategic Questions

List specific questions you want answered:

1. Should I build another settlement or save for a city?
2. Is it worth trading heavily for specific resources?
3. Should I prioritise blocking opponent or growing my position?
4. When should I play my development card?
