---
command: fix-rules
version: "1.0"

metadata:
  name: "Fix Rules Template"
  description: "Identify missing, ambiguous, or flawed rules and suggest corrections"

context:
  # Optional: Provide context about known issues
  # game_type: "Dice-based adventure game"
  # known_issues:  # Issues reported by players
  #   - "Combat resolution unclear when dice tie"
  #   - "Trading timing is ambiguous"
  # playtester_feedback: |
  #   Players were confused about turn order after special events.

parameters:
  # Optional: Output settings
  format: markdown  # Options: markdown, json
  # output_file: "results/rule-fixes.md"  # Uncomment to save to file

  # Optional: Focus areas
  # focus_areas:  # Specific rule sections to examine
  #   - "Combat mechanics"
  #   - "Trading rules"
  #   - "Victory conditions"

content:
  # Option 1: Reference a rulebook file
  rules_file: "path/to/rulebook.pdf"

  # Option 2: Paste rules inline (remove rules_file if using this)
  # rules: |
  #   # Your rulebook content here

---

# Known Ambiguities

List specific ambiguities or questions here:

1. What happens when [specific situation]?
2. Is [action] allowed during [phase]?
3. How is [tie/conflict] resolved?
