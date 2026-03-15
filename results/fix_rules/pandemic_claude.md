---
game: pandemic
model: claude-opus-4
task: fix_rules
---

ISSUES IDENTIFIED:

1. **Setup step numbering is out of order in the raw rulebook.** Steps 8 and 9 (dividing Player cards into piles and shuffling Epidemic cards in) appear before steps 6 and 7 (pulling Epidemic cards out and dealing Player cards). The printed layout jumbles the numbered sequence, making it confusing to follow setup linearly.

2. **Player count vs. cards dealt table is ambiguous.** The rulebook presents "PLAYER GAME: CARDS EACH" three times with paired numbers (4/2, 3/3, 2/4) but never explicitly labels which number is the player count and which is the card count. A new player must infer that 2 players get 4 cards, 3 players get 3 cards, and 4 players get 2 cards.

3. **Shuttle Flight does not mention discarding a card.** The Drive/Ferry, Direct Flight, and Charter Flight actions all specify what happens with cards, but Shuttle Flight simply says to move between Research Stations with no mention of whether a card is needed or discarded. While this is correct (no card is required), the omission breaks the parallel structure and could cause confusion.

4. **Share Knowledge action direction is ambiguous.** The rules say "Transfer a card from one player to another" and that "you may only transfer the card of the city that you are in together," but do not clearly specify whether the active player must be the giver, the receiver, or either. Only the Researcher exception text implies that both giving and receiving are possible.

5. **Epidemic step ordering is inconsistent between the detailed rules and the visual summary.** The detailed rules list the three Epidemic steps as (1) Increase, (2) Intensify, (3) Infect. However, the correct and commonly played order is (1) Increase, (2) Infect (draw bottom card), (3) Intensify (shuffle discard pile on top). The numbered labels in the raw text place "Intensify" as step 3 and "Infect" as step 2, but the visual diagram sidebar reverses this. This is a significant source of play errors.

6. **No explicit rule for what happens when drawing 2 Player cards and the first is an Epidemic.** The rules say to draw 2 cards and resolve Epidemics, but do not clarify whether the player draws the second card before or after resolving the Epidemic triggered by the first card. (The correct procedure is to fully resolve the first Epidemic before drawing the second card.)

7. **Eradication is described under Treat Disease but its passive trigger is unclear.** The rules state that when all cubes of a cured color are removed, the disease is eradicated. However, they do not specify that this check happens immediately and automatically whenever the last cube is removed (including via outbreaks, Medic passive ability, or other indirect means).

8. **The Medic's passive ability timing is vague.** The rules say the Medic "at any time" removes cubes of a cured disease from her city, and that this is "in effect during all players' turns." It is unclear whether this triggers when the Medic is moved by the Dispatcher, or when cubes are placed in the Medic's city during infection. (Both should trigger the ability.)

9. **Missing rule for 5-player games.** The component list includes 5 pawns and 5 role cards, but the card dealing table only covers 2, 3, and 4 players. There is no guidance for a 5-player game (which would presumably deal 2 cards each, same as 4 players, but this is never stated).

10. **Chain reaction outbreak rule lacks clarity on cube color.** The rules say outbreaks add cubes "of the outbreaking color" to adjacent cities, but during chain reactions involving multiple colors, it could be ambiguous which color propagates. The rule should emphasize that the color of the cube causing each individual outbreak is always the color that spreads.

11. **Special Event card timing is insufficiently defined.** The rules say Special Event cards "may be played at any time (even on a fellow player's turn)" but do not specify whether they can interrupt an Epidemic resolution, an outbreak chain reaction, or the infection step. The only restriction mentioned is that they do not cost an action.

12. **"Te" appears throughout the text instead of "The."** This is a consistent OCR or encoding artifact from the original PDF extraction, rendering every instance of "The" as "Te."


SUGGESTED FIXES:

1. **Renumber setup steps sequentially:** Present setup as steps 1 through 12 in logical order: (1) Place board, (2) Deal roles and place pawns in Atlanta, (3) Place Research Station in Atlanta, (4) Place markers, (5) Sort disease cubes, (6) Pull Epidemic cards aside, (7) Deal Player cards by player count, (8) Divide remaining Player cards into piles by difficulty, (9) Shuffle one Epidemic card into each pile and stack, (10) Shuffle and place Infection Draw Pile, (11) Seed initial infections (3/2/1 cubes), (12) Most recently sick player goes first.

2. **Reformat the card dealing table** with explicit headers: "Number of Players: 2 -> Deal 4 cards each | 3 -> Deal 3 cards each | 4 -> Deal 2 cards each."

3. **Add a clarifying note to Shuttle Flight:** "No card is required or discarded for this action."

4. **Clarify Share Knowledge direction:** "Either the active player gives a card to a co-located player, or receives a card from a co-located player. In both cases, only the card matching the shared city may be transferred."

5. **Fix Epidemic step order to match correct gameplay:** "(1) Increase: advance the Infection Rate Marker. (2) Infect: draw the bottom card of the Infection Draw Pile, add 3 cubes to that city, discard the card. (3) Intensify: shuffle the entire Infection Discard Pile and place it on top of the Infection Draw Pile."

6. **Add sequential draw clarification:** "When drawing 2 Player cards, draw and fully resolve each card one at a time. If the first card drawn is an Epidemic, resolve it completely before drawing the second card."

7. **Make eradication trigger explicit:** "Whenever the last cube of a cured disease color is removed from the board by any means (Treat Disease action, Medic ability, or any other effect), that disease is immediately eradicated."

8. **Clarify Medic passive ability scope:** "The Medic automatically removes all cubes of any cured disease from the city she occupies. This triggers immediately whenever the Medic enters a city (including when moved by the Dispatcher) and whenever cubes of a cured disease are placed in the Medic's current city during infection."

9. **Add 5-player rule or clarify component intent:** "The game supports 2 to 4 players. The 5th pawn and role card are included for variety in role selection; deal 2 cards each in a 4-player game." Alternatively, if 5-player games are intended, add: "5 players: deal 2 cards each."

10. **Clarify chain reaction cube color:** "During a chain reaction, each outbreak spreads cubes of the specific color that caused that particular outbreak. If a city outbreaks in black, black cubes are added to all adjacent cities, even if the original triggering outbreak was a different color."

11. **Define Special Event timing windows:** "Special Event cards may be played at any time, including during another player's turn, between drawing Infection cards, or between resolving the steps of an Epidemic. They may not interrupt the resolution of a single outbreak."

12. **Fix all "Te" occurrences** to read "The" throughout the rulebook.


CORRECTED RULES:

### Setup (Corrected Sequence)

1. Place the Board in the center of the table within easy reach of all players.
2. Shuffle the Role cards and deal 1 to each player. Each player takes the corresponding pawn and places it in Atlanta. Return excess Role cards and pawns to the box.
3. Place 1 Research Station in Atlanta. Place the remaining Research Stations near the side of the board.
4. Place the Outbreaks Marker on the "0" space of the Outbreaks Indicator. Place the Infection Rate Marker on the first space of the Infection Rate Track (marked "2"). Place the 4 Cure Markers (vial-side up) near the Cures Discovered Area.
5. Separate Disease cubes by color and place them in four piles near the board.
6. Pull the 6 Epidemic cards out of the Player card deck and set them aside.
7. Shuffle the remaining Player cards and deal face down to each player: 2 players = 4 cards each; 3 players = 3 cards each; 4 players = 2 cards each.
8. Divide the remaining Player cards into equal piles based on difficulty: Introductory = 4 piles; Normal = 5 piles; Heroic = 6 piles.
9. Shuffle 1 Epidemic card (face down) into each pile. Stack the piles to form the Player Draw Pile, with larger piles on top of smaller piles. Return any excess Epidemic cards to the box.
10. Shuffle the Infection cards and place them face down on the board as the Infection Draw Pile.
11. Seed initial infections: (a) Draw 3 Infection cards, place 3 cubes of the matching color on each city, and discard the cards. (b) Draw 3 more cards, place 2 cubes each, and discard. (c) Draw 3 final cards, place 1 cube each, and discard. All discarded cards go to the Infection Discard Pile.
12. The player who was most recently sick goes first.

### Shuttle Flight (Corrected)

**Shuttle Flight:** If your pawn is in a city with a Research Station, move it to any other city with a Research Station. No card is required or discarded for this action.

### Share Knowledge (Corrected)

**Share Knowledge:** Transfer a card between two players whose pawns are in the same city. The active player may either give or receive the card. Only the card matching the city both players occupy may be transferred. Each card transferred costs 1 action. If either player exceeds the 7-card hand limit as a result, excess cards must be immediately discarded to the Player Discard Pile.

The Researcher may give any card from his hand (not restricted to the current city card) during a Share Knowledge action. This applies only when the Researcher is the giver. When receiving, the Researcher follows the normal restriction.

### Epidemics (Corrected Step Order)

When a player draws an Epidemic card, discard it to the Player Discard Pile and resolve the following three steps in order:

1. **Increase:** Advance the Infection Rate Marker one space on the Infection Rate Track.
2. **Infect:** Draw the bottom card from the Infection Draw Pile. Add 3 disease cubes of the matching color to the pictured city. If this would cause the city to exceed 3 cubes of that color, add cubes up to 3 and trigger an outbreak (see Outbreaks). Discard the drawn card to the Infection Discard Pile.
3. **Intensify:** Take the entire Infection Discard Pile, shuffle it thoroughly, and place it face down on top of the remaining Infection Draw Pile. Do not shuffle these cards into the draw pile.

If there are not enough cubes to place during step 2, the game immediately ends in defeat.

### Drawing Cards (Corrected)

After completing 4 actions, draw 2 cards one at a time from the Player Draw Pile. If a drawn card is an Epidemic, resolve it fully (all three Epidemic steps) before drawing the next card. Non-Epidemic cards are added to your hand. If there are not enough cards in the Player Draw Pile to complete the draw, the game immediately ends in defeat.

### Medic (Corrected)

**Medic:** When performing the Treat Disease action, the Medic removes all cubes of a single color from the current city (instead of just 1). Additionally, whenever the Medic enters or is moved to a city containing cubes of a cured disease, all cubes of that cured color are immediately removed at no action cost. This passive ability also triggers if cubes of a cured disease are placed in the Medic's current city during infection. This ability is active during all players' turns.

### Eradication (Corrected)

If a cure for a disease has been discovered and all cubes of that color have been removed from the board by any means, the disease is immediately eradicated. Flip the corresponding Cure Marker to the "Sunset" side. From this point on, Infection cards of this color have no effect: no cubes are placed during the Infector step or during Epidemics. Return all cubes of the eradicated color to the box.

### Chain Reaction Outbreaks (Corrected)

When an outbreak occurs, add 1 cube of the outbreaking color to each adjacent city. If this causes any adjacent city to exceed 3 cubes of that same color, a chain reaction outbreak occurs in that city. During a chain reaction, each city may outbreak at most once. The color that spreads from each outbreak is always the color that triggered that specific outbreak. Advance the Outbreaks Marker once for each individual outbreak in the chain.
