---
command: explain
version: "1.0"

metadata:
  name: "Simple Explain Example"
  description: "A minimal working example of an explain template"

context:
  theme: "Card game"

parameters:
  audience: child
  format: markdown

content:
  rules: |
    # Simple Card Game

    ## Setup
    Each player receives 5 cards from the deck.

    ## Gameplay
    On your turn:
    1. Draw a card
    2. Play a card
    3. Discard if you have more than 7 cards

    ## Winning
    First player to play all their cards wins!
---

# Additional Notes

This is a very simple card game designed to demonstrate the template system.
The explanation should be tailored for children aged 8-12.
