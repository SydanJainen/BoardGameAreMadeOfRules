---
model: mistral-nemo:12b
temperature: 0.8
timestamp: '2026-02-18T14:04:02.327883Z'
execution_time_seconds: 45.62
prompt_length: 38944
model_alias: mistral
tokens: 1060
---

# Rule Explanation for Expert Audience

**Pandemic Board Game Rules (Expert Version)**

*Pandemic* is a cooperative board game designed by Matt Leacock and published by Z-Man Games. Here are the rules for an expert audience:

**Game Components:**

1. 48 Infection Cards
2. 5 Role Cards
3. 4 Reference Cards
4. Game Board
5. Four Cure Markers (vial-side)
6. Outbreak Marker
7. Infection Rate Marker
8. Player Discard Pile & Draw Pile
9. Infection Discard Pile & Draw Pile
10. Research Station Tokens
11. Disease Cubes (24 each of yellow, red, blue, black)

**Setup:**

1. Place the game board in the center of the table.
2. Shuffle the Infection Cards and place them face down near the board to form the Infection Draw Pile.
3. Shuffle the Player Cards (Including Special Event cards) and deal each player 4 cards from this deck to form their initial hands, then create the Player Discard Pile & Draw Pile.
4. Place the Research Station Tokens, Cure Markers, Outbreak Marker, Infection Rate Marker, and Disease Cubes near the board.
5. Assign a Role Card to each player (see below for role descriptions).
6. Choose one of the four starting scenarios or create your own.

**Gameplay:**

1. **Player Turns:** Players take turns in clockwise order, performing actions based on their role's abilities.
2. **Actions:**
   - *Move:* Move your pawn to an adjacent city, treating disease there if present.
   - *Treat Disease:* Remove cubes from a city (either yours or another player's).
   - *Discover Cure:* Discard cards of the corresponding color equal to the number on the Cure Markers space +1. Place the Cure Marker vial-side up.
   - *Build Research Station:* Spend an action and discard a card of the city where you want to build it.
   - *Share Knowledge:* Trade one card from your hand with another player, not revealing what cards are in play (except Introductory Game).
   - *Charter Flight:* Discard a card of any city, move your pawn there. *Flight Charter:* Spend an action and two cards to perform this action.
3. **Epidemic Phase:** After each player's turn, draw cards equal to the current infection rate (Infection Rate Marker). Resolve these cards in order:
   - Increase infection rate: Move the Infection Rate Marker up one space.
   - Shuffle the Infection Discard Pile and place it on top of the remaining Infection Draw Pile.
   - Infect cities: Add three cubes to each city pictured on the drawn card(s), placing them into the Infection Discard Pile afterward. If a city has 3 cubes of any color, an outbreak occurs (see below).
4. **Outbreaks:** When a city outbreaks, add one cube of the outbreaking color to each adjacent city. Move the Outbreak Marker up one space on the Outbreak Indicator. If the Outbreak Marker reaches the skull symbol (8th outbreak), the game ends immediately in defeat.
5. **Epidemics:** Whenever a player draws an Epidemic card, do the following:
   - Discard it into the Player Discard Pile.
   - Increase infection rate: Move the Infection Rate Marker up one space.
   - Increase infection intensity: Shuffle the Infection Discard Pile and place it on top of the remaining Infection Draw Pile.
   - Infect cities: Take the bottom card from the Infection Draw Pile, add three cubes to the city pictured on that card, then place the card into the Infection Discard Pile. If adding cubes would cause a city to have more than 3 cubes of any one color, return excess cubes and trigger an outbreak.
6. **Player Cards Hand Limit:** Players cannot end their turn with more than seven cards in hand. Discard excess cards or play Special Event cards (which do not count towards the limit).
7. **Winning the Game:** Cures for all four diseases have been discovered, ending the game immediately in victory. Players collectively win when any player discovers the fourth and final cure.

**Roles:**

1. **Medic:** Move without drawing Infection Cards, treat disease from two different cities simultaneously.
2. **Scientist:** Discover cures using only four cards of a single color (instead of five).
3. **Operations Expert:** Build Research Stations spending only one action instead of two.
4. **Dispatcher:** Move to any city once per turn without drawing Infection Cards, may give this movement ability to another player's pawn once per game.

**Game End:**

The game ends immediately in defeat when:

1. Players collectively win by discovering all four cures.
2. The eighth outbreak occurs (Outbreaks Marker reaches the skull symbol).
3. A player must draw cards but cannot because there are none left in the Player Draw Pile.

*For additional rules and clarifications, please consult the official rulebook or contact Z-Man Games.*

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
**Pandemic Board Game Rules (Expert Version)**

*Pandemic* is a cooperative board game designed by Matt Leacock and published by Z-Man Games. Here are the rules for an expert audience:

**Game Components:**

1. 48 Infection Cards
2. 5 Role Cards
3. 4 Reference Cards
4. Game Board
5. Four Cure Markers (vial-side)
6. Outbreak Marker
7. Infection Rate Marker
8. Player Discard Pile & Draw Pile
9. Infection Discard Pile & Draw Pile
10. Research Station Tokens
11. Disease Cubes (24 each of yellow, red, blue, black)

**Setup:**

1. Place the game board in the center of the table.
2. Shuffle the Infection Cards and place them face down near the board to form the Infection Draw Pile.
3. Shuffle the Player Cards (Including Special Event cards) and deal each player 4 cards from this deck to form their initial hands, then create the Player Discard Pile & Draw Pile.
4. Place the Research Station Tokens, Cure Markers, Outbreak Marker, Infection Rate Marker, and Disease Cubes near the board.
5. Assign a Role Card to each player (see below for role descriptions).
6. Choose one of the four starting scenarios or create your own.

**Gameplay:**

1. **Player Turns:** Players take turns in clockwise order, performing actions based on their role's abilities.
2. **Actions:**
   - *Move:* Move your pawn to an adjacent city, treating disease there if present.
   - *Treat Disease:* Remove cubes from a city (either yours or another player's).
   - *Discover Cure:* Discard cards of the corresponding color equal to the number on the Cure Markers space +1. Place the Cure Marker vial-side up.
   - *Build Research Station:* Spend an action and discard a card of the city where you want to build it.
   - *Share Knowledge:* Trade one card from your hand with another player, not revealing what cards are in play (except Introductory Game).
   - *Charter Flight:* Discard a card of any city, move your pawn there. *Flight Charter:* Spend an action and two cards to perform this action.
3. **Epidemic Phase:** After each player's turn, draw cards equal to the current infection rate (Infection Rate Marker). Resolve these cards in order:
   - Increase infection rate: Move the Infection Rate Marker up one space.
   - Shuffle the Infection Discard Pile and place it on top of the remaining Infection Draw Pile.
   - Infect cities: Add three cubes to each city pictured on the drawn card(s), placing them into the Infection Discard Pile afterward. If a city has 3 cubes of any color, an outbreak occurs (see below).
4. **Outbreaks:** When a city outbreaks, add one cube of the outbreaking color to each adjacent city. Move the Outbreak Marker up one space on the Outbreak Indicator. If the Outbreak Marker reaches the skull symbol (8th outbreak), the game ends immediately in defeat.
5. **Epidemics:** Whenever a player draws an Epidemic card, do the following:
   - Discard it into the Player Discard Pile.
   - Increase infection rate: Move the Infection Rate Marker up one space.
   - Increase infection intensity: Shuffle the Infection Discard Pile and place it on top of the remaining Infection Draw Pile.
   - Infect cities: Take the bottom card from the Infection Draw Pile, add three cubes to the city pictured on that card, then place the card into the Infection Discard Pile. If adding cubes would cause a city to have more than 3 cubes of any one color, return excess cubes and trigger an outbreak.
6. **Player Cards Hand Limit:** Players cannot end their turn with more than seven cards in hand. Discard excess cards or play Special Event cards (which do not count towards the limit).
7. **Winning the Game:** Cures for all four diseases have been discovered, ending the game immediately in victory. Players collectively win when any player discovers the fourth and final cure.

**Roles:**

1. **Medic:** Move without drawing Infection Cards, treat disease from two different cities simultaneously.
2. **Scientist:** Discover cures using only four cards of a single color (instead of five).
3. **Operations Expert:** Build Research Stations spending only one action instead of two.
4. **Dispatcher:** Move to any city once per turn without drawing Infection Cards, may give this movement ability to another player's pawn once per game.

**Game End:**

The game ends immediately in defeat when:

1. Players collectively win by discovering all four cures.
2. The eighth outbreak occurs (Outbreaks Marker reaches the skull symbol).
3. A player must draw cards but cannot because there are none left in the Player Draw Pile.

*For additional rules and clarifications, please consult the official rulebook or contact Z-Man Games.*
```

</details>
