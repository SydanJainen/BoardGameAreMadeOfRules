---
command: invent
version: "1.0"

metadata:
  name: "Invent Game Template"
  description: "Generate a new boardgame design based on a concept or theme"
  # author: "Your name"

# OPTIONAL: Custom prompt (replaces the standard prompt body).
# The system preamble and format instructions are always included.
# custom_prompt: |
#   Your free-form prompt here. Describe in detail the game you want.
#   Format instructions will be appended automatically so the output
#   remains parseable.

# OPTIONAL: Path to external prompt file (takes priority over custom_prompt).
# Can be absolute or relative to project root.
# prompt_file: "prompts/my_custom_prompt.txt"

context:
  # Optional: Provide thematic and design context
  theme: ""  # Specific theme/setting (e.g., "Space archaeology")
  # target_audience: "Casual gamers, age 12+"  # Who the game is for
  # inspiration:  # Reference games
  #   - "Pandemic (cooperative)"
  #   - "Ticket to Ride (set collection)"
  # setting: |
  #   Year 2250. Players explore alien ruins...

parameters:
  # Optional: Design constraints
  # mechanics:  # Preferred/required mechanics
  #   - "Set collection"
  #   - "Area control"
  # complexity: 2.5  # 1-5 scale (1=simple, 5=very complex)
  # player_count: "2-4"  # Desired player range
  # duration: "45-60"  # Target game length in minutes

  # Optional: Component constraints
  # components:
  #   max_cards: 100
  #   max_tokens: 50
  #   board_type: "Modular tiles"

  # Optional: Output settings
  format: markdown  # Options: markdown, json
  # output_file: "results/new-game.md"  # Uncomment to save to file

content:
  # Required: Game idea summary (use idea_summary, not concept)
  idea_summary: |
    A brief summary of your game idea. For example:

    "A cooperative game where players explore ancient alien ruins,
    collect artefacts, and piece together the story of a lost civilisation.
    The twist: artefacts are more valuable when you understand their
    cultural context."

  # Optional: Design constraints
  # design_constraints: |
  #   - Must be playable on a table (no app required)
  #   - Should work both competitively and cooperatively
  #   - Avoid excessive downtime between turns

---

# Design Goals

Describe what you want from this game:

1. Thematic immersion - mechanics should evoke [theme]
2. Strategic depth - multiple paths to victory
3. Accessibility - easy to teach, hard to master
4. Replayability - variable setup or modular components
