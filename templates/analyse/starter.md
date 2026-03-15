---
command: analyse
version: "1.0"

metadata:
  name: "Analyse Game Template"
  description: "Extract game properties and compare with BoardGameGeek data"

context:
  # Optional: Provide hints to improve analysis accuracy
  # expected_complexity: 2.5  # 1-5 scale (1=simple, 5=very complex)
  # expected_mechanics:  # Mechanics you expect to find
  #   - "Card drafting"
  #   - "Engine building"


parameters:
  # Optional: BoardGameGeek comparison
  # bgg_id: 266192 

  # Optional: Output settings
  format: markdown  # Options: markdown, json
  # output_file: "results/analysis.md" 

content:
  # Option 1: Reference a rulebook file
  rules_file: "path/to/rulebook.pdf"

  # Option 2: Paste rules inline (remove rules_file if using this)
  # rules: |
  #   # Your rulebook content here

---

# Analysis Notes

Add any specific areas you want the analysis to focus on:

- Engine-building mechanics
- Decision complexity
- Player interaction patterns
- Resource management systems
