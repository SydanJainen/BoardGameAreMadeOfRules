---
model: qwen2.5:latest
temperature: 0.6
timestamp: '2026-02-18T13:56:22.768111Z'
execution_time_seconds: 25.49
prompt_length: 7812
model_alias: qwen
tokens: 1025
---

# Rule Explanation for Expert Audience

### Century: A Detailed Rule Explanation

**Setup**
1. **Point Cards (Deck A & B):** Shuffle all Point cards to form a deck (A), then draw 5 cards and place them face up in a row to the left of this deck (B). This forms your initial view of potential point cards.
2. **Token Piles:** Place two times the number of players' tokens above each of the first two Point cards as indicated (C & D).
3. **Merchant Cards (Deck E):** Among Merchant cards, 10 are face up with a purple border and are considered starting cards. Each player receives one 'Create 2' and one 'Upgrade 2', while any remaining cards go back into the box.
4. **Remaining Merchant Cards:** Shuffle these to form another deck (E). Draw six more cards and place them face up in a row to the left of this new deck (F).
5. **Spice Cubes:** Separate cubes by color (yellow, red, green, brown) and place them into bowls according to their order: Yellow (Turmeric), Red (Saffron), Green (Cardamom), Brown (Cinnamon).
6. **Caravan Cards & First Player Determination:** Each player receives one Caravan card with a first-player symbol shuffled from the deck of such cards, ensuring that each player has an equal chance to start.
7. **Initial Cube Placement on Caravans:** Place cubes as per the table based on player order: 1st (3 yellow), 2nd & 3rd (4 yellow), 4th & 5th (3 yellow and 1 red).

**Gameplay Mechanics**
1. **Action Selections:**
   - **Play:** Players can play any card from their hand, executing its effect.
     - **Spice Cards:** Take the indicated number of cubes from the bowls and place them on your caravan.
     - **Upgrade Cards:** Upgrade one or two cubes as per the card's instruction. The upgrade levels are: yellow (1), red (2), green (3).
     - **Trade Cards:** Exchange specified cubes between your caravan and the supply, with the ability to perform multiple trades in a row if you have sufficient cubes.
   - **Acquire:** Purchase a Merchant card by placing cubes on each of the cards to its left. This action adds the acquired card to your hand but also moves other cards up and draws a new one from the deck.
   - **Rest:** Return all played cards back into your hand, allowing for strategic planning in future turns.

2. **Caravan Limit:** At the end of each turn, if you exceed 10 cubes on your caravan, you must return excess cubes to their respective bowls until you have exactly 10 cubes.
3. **Cube Limit:** The supply is virtually unlimited, though players can use substitute materials (like candy) for additional cubes.

**Objective & Scoring**
- **Claiming Point Cards:** To claim a point card, you must have all the required cubes on your caravan. Once claimed, return these cubes to their respective bowls and take the card face down in front of you.
  - Claiming the leftmost or second-leftmost Point cards grants gold/silver tokens (1 token per player).
  - If the last gold token is taken, move the silver token pile above the leftmost Point card.
- **Endgame:** The game ends once a player has claimed their fifth (or sixth in a 2-3 player game) point card. At this point, count points from:
  - Points on claimed cards.
  - Gold and silver tokens: 1 gold = 3 points; 1 silver = 1 point.
  - Non-yellow cubes remaining on your caravan: 1 cube = 1 point.

### Strategic Considerations
- **Cube Management:** Efficiently managing cubes is crucial. Prioritize upgrading to higher-value cubes (red, green) and use trades wisely to maximize cube count.
- **Card Acquisition Strategy:** Acquiring cards strategically based on their effects can significantly impact your gameplay. Balance immediate benefits with long-term strategic plays.
- **Point Card Claims:** Targeting specific point cards early in the game can provide a significant advantage by securing valuable tokens or cubes.

### Edge Cases & Rule Interactions
- **Token Scarcity:** If token piles run out, they are not replenished; thus, managing these resources carefully is essential.
- **Caravan Overfilling:** Players must be mindful of their caravan's capacity. Exceeding the limit results in automatic cube return to bowls until the correct number is achieved.
- **Trade Card Limitations:** Ensure you have enough cubes available for multiple trades to fully utilize trade cards.

### Conclusion
Century offers a rich and strategic experience through its combination of resource management, card drafting, and point collection. The game's mechanics encourage thoughtful planning and adaptability, making it a compelling choice for experienced board gamers seeking depth and complexity in their gameplay.

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
### Century: A Detailed Rule Explanation

**Setup**
1. **Point Cards (Deck A & B):** Shuffle all Point cards to form a deck (A), then draw 5 cards and place them face up in a row to the left of this deck (B). This forms your initial view of potential point cards.
2. **Token Piles:** Place two times the number of players' tokens above each of the first two Point cards as indicated (C & D).
3. **Merchant Cards (Deck E):** Among Merchant cards, 10 are face up with a purple border and are considered starting cards. Each player receives one 'Create 2' and one 'Upgrade 2', while any remaining cards go back into the box.
4. **Remaining Merchant Cards:** Shuffle these to form another deck (E). Draw six more cards and place them face up in a row to the left of this new deck (F).
5. **Spice Cubes:** Separate cubes by color (yellow, red, green, brown) and place them into bowls according to their order: Yellow (Turmeric), Red (Saffron), Green (Cardamom), Brown (Cinnamon).
6. **Caravan Cards & First Player Determination:** Each player receives one Caravan card with a first-player symbol shuffled from the deck of such cards, ensuring that each player has an equal chance to start.
7. **Initial Cube Placement on Caravans:** Place cubes as per the table based on player order: 1st (3 yellow), 2nd & 3rd (4 yellow), 4th & 5th (3 yellow and 1 red).

**Gameplay Mechanics**
1. **Action Selections:**
   - **Play:** Players can play any card from their hand, executing its effect.
     - **Spice Cards:** Take the indicated number of cubes from the bowls and place them on your caravan.
     - **Upgrade Cards:** Upgrade one or two cubes as per the card's instruction. The upgrade levels are: yellow (1), red (2), green (3).
     - **Trade Cards:** Exchange specified cubes between your caravan and the supply, with the ability to perform multiple trades in a row if you have sufficient cubes.
   - **Acquire:** Purchase a Merchant card by placing cubes on each of the cards to its left. This action adds the acquired card to your hand but also moves other cards up and draws a new one from the deck.
   - **Rest:** Return all played cards back into your hand, allowing for strategic planning in future turns.

2. **Caravan Limit:** At the end of each turn, if you exceed 10 cubes on your caravan, you must return excess cubes to their respective bowls until you have exactly 10 cubes.
3. **Cube Limit:** The supply is virtually unlimited, though players can use substitute materials (like candy) for additional cubes.

**Objective & Scoring**
- **Claiming Point Cards:** To claim a point card, you must have all the required cubes on your caravan. Once claimed, return these cubes to their respective bowls and take the card face down in front of you.
  - Claiming the leftmost or second-leftmost Point cards grants gold/silver tokens (1 token per player).
  - If the last gold token is taken, move the silver token pile above the leftmost Point card.
- **Endgame:** The game ends once a player has claimed their fifth (or sixth in a 2-3 player game) point card. At this point, count points from:
  - Points on claimed cards.
  - Gold and silver tokens: 1 gold = 3 points; 1 silver = 1 point.
  - Non-yellow cubes remaining on your caravan: 1 cube = 1 point.

### Strategic Considerations
- **Cube Management:** Efficiently managing cubes is crucial. Prioritize upgrading to higher-value cubes (red, green) and use trades wisely to maximize cube count.
- **Card Acquisition Strategy:** Acquiring cards strategically based on their effects can significantly impact your gameplay. Balance immediate benefits with long-term strategic plays.
- **Point Card Claims:** Targeting specific point cards early in the game can provide a significant advantage by securing valuable tokens or cubes.

### Edge Cases & Rule Interactions
- **Token Scarcity:** If token piles run out, they are not replenished; thus, managing these resources carefully is essential.
- **Caravan Overfilling:** Players must be mindful of their caravan's capacity. Exceeding the limit results in automatic cube return to bowls until the correct number is achieved.
- **Trade Card Limitations:** Ensure you have enough cubes available for multiple trades to fully utilize trade cards.

### Conclusion
Century offers a rich and strategic experience through its combination of resource management, card drafting, and point collection. The game's mechanics encourage thoughtful planning and adaptability, making it a compelling choice for experienced board gamers seeking depth and complexity in their gameplay.
```

</details>
