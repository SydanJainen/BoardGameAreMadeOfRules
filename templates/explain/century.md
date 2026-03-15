---
command: explain
version: "1.0"

metadata:
  name: "Explain Rules Template"
  description: "Generate audience-specific explanations of boardgame rules"

parameters:
  audience: child  # child, adult, expert

  # Optional: Output settings
  format: markdown  # Options: markdown, json
  output_file: "results/century/child-explanation.md"  # comment to display in CLI

  # Optional: Explanation customisation
  simplification_level: 3  # 1 (minimal) to 5 (maximum simplification)
  include_examples: true 
  focus_areas: 
     - "Victory conditions"

content:
  # Option 1: Reference a rulebook file
  rules_file: "./rulebooks/century.pdf"

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

