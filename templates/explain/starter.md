---
command: explain
version: "1.0"

metadata:
  name: "Explain Rules Template"
  description: "Generate audience-specific explanations of boardgame rules"
  # author: "Your name"

context:
  # Optional: Add context to help the LLM understand the game better
  theme: ""  # Game theme/setting (e.g., "Medieval trading", "Space exploration")
  background: ""  # Additional background information about the game

parameters:
  # Required: Target audience
  audience: adult  # Options: child (8-12), adult (13+), expert (experienced gamers)

  # Optional: Output settings
  format: markdown  # Options: markdown, json
  # output_file: "results/explanation.md"  # Uncomment to save to file

  # Optional: Explanation customisation
  # simplification_level: 3  # 1 (minimal) to 5 (maximum simplification)
  # include_examples: true  # Add concrete examples
  # focus_areas:  # Specific rules to emphasise
  #   - "Resource gathering"
  #   - "Victory conditions"

content:
  # Option 1: Reference a rulebook file
  rules_file: "path/to/rulebook.pdf"

  # Option 2: Paste rules inline (remove rules_file if using this)
  # rules: |
  #   # Your rulebook content here
  #
  #   ## Setup
  #   Each player receives...
  #
  #   ## Turn Structure
  #   On your turn, you may...

---

# Additional Notes

You can add additional notes here in Markdown format to guide the explanation.

For example:
- Focus on these key concepts: [list concepts]
- Avoid these complex topics: [list topics]
- Compare to these familiar games: [list games]
