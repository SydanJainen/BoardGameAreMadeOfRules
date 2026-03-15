---
model: qwen2.5:latest
temperature: 0.6
timestamp: '2026-02-18T14:03:00.423368Z'
execution_time_seconds: 28.74
prompt_length: 38935
model_alias: qwen
tokens: 933
---

# Rule Explanation for Adult Audience

### Pandemic Board Game Rules Overview

**Objective**: The objective is to work together as a team to discover cures for four deadly diseases (Blue, Yellow, Black, and Red) before they spread globally. You must manage disease outbreaks, build research stations, and use the unique abilities of your roles to save humanity.

### Setup
1. **Divide Player Cards**: 
   - For the Introductory Game: Divide cards into 4 piles.
   - For Normal Game: Divide cards into 5 piles.
   - For Heroic Game: Divide cards into 6 piles (once you've mastered Normal).
2. **Shuffle and Deal Role Cards**:
   - Each player gets one role card and a corresponding pawn, which is placed in Atlanta.
3. **Place Initial Resources**: 
   - Place 1 Research Station in Atlanta.
   - Place other Research Stations near the side of the board.
4. **Place Trackers**:
   - Put the Outbreaks Marker on “0” on the Outbreak Indicator.
   - Put the Infection Rate Marker on “2” (first space) on the Infection Rate Track.
   - Place 4 Cure Markers near the Cures Discovered Area.
5. **Separate Disease Cubes**:
   - Place them in four piles by color (Blue, Yellow, Black, Red).
6. **Epidemic Cards**: Pull out and set aside 6 Epidemic cards for now.
7. **Infection Draw Pile**: Shuffle the Infection cards (green back) and place them face down on the board to form the Infection Draw Pile.

### Infection Phase
1. **Draw Infection Cards**:
   - The Infector draws a number of Infection cards based on the Infection Rate.
2. - Each card drawn adds disease cubes to the pictured cities using matching colored cubes.
3. - If a city already has 3 cubes, an outbreak occurs (adding cubes to adjacent cities).
4. - Outbreaks continue if any new cubes would cause a city to exceed 3.

### Player Turn
1. **Actions**:
   - Each player gets 4 actions per turn.
2. **Available Actions**: 
   - Charter Flight: Move your pawn by playing the card corresponding to your current location.
   - Shuttle Flight: Move from any Research Station in your current city to another with a Research Station.
   - Direct Flight: Move to an adjacent city using a card from your hand.
   - Drive (or Ferry): Move to an adjacent city without a card.
   - Treat Disease: Remove one disease cube from the city you occupy, or all cubes if the Medic and in a cured disease city.
   - Discover A Cure: Requires 4 cards of the correct color for the Scientist; otherwise, needs 5. Place cure marker vial-side up when done.
   - Build Research Station: Use a card to build one at your current location.
   - Share Knowledge: Transfer a card from another player in the same city (unique ability: Researcher can give any card).
3. **Special Actions**:
   - Scientist: Discover cures with 4 cards of the correct color instead of 5.
   - Operations Expert: Build Research Station without playing a matching card.
   - Dispatcher: Move other players' pawns as if they were your own.

### Player Draw Phase
1. **Draw Cards**: After actions, draw 2 cards from the Player Draw Pile unless it’s an Epidemic card (discard and follow its instructions).

### Playing the Infector
1. **Epidemic**:
   - If there aren’t enough cubes to add, immediately end the game.
2. **Infection Rate**: Increase as per rules if drawing an Epidemic card.
3. **Draw Infection Cards**: Draw cards equal to the current Infection Rate and place them on the board.

### Winning Conditions
1. **Discover Cures**: 
   - Once all four cures are discovered (vial-side up), you win immediately.
2. **Defeat**:
   - If the Outbreaks Marker reaches 8 or if there aren’t enough cubes for Infection or drawing cards, the game ends in defeat.

### Strategy and Play
- Communicate effectively with your team to manage resources and outbreaks efficiently.
- Use special abilities wisely based on each role's unique strengths.
- Manage your hand size (7 cards) by discarding excess cards if needed.

Enjoy the challenge of working together as a disease-fighting team!

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
### Pandemic Board Game Rules Overview

**Objective**: The objective is to work together as a team to discover cures for four deadly diseases (Blue, Yellow, Black, and Red) before they spread globally. You must manage disease outbreaks, build research stations, and use the unique abilities of your roles to save humanity.

### Setup
1. **Divide Player Cards**: 
   - For the Introductory Game: Divide cards into 4 piles.
   - For Normal Game: Divide cards into 5 piles.
   - For Heroic Game: Divide cards into 6 piles (once you've mastered Normal).
2. **Shuffle and Deal Role Cards**:
   - Each player gets one role card and a corresponding pawn, which is placed in Atlanta.
3. **Place Initial Resources**: 
   - Place 1 Research Station in Atlanta.
   - Place other Research Stations near the side of the board.
4. **Place Trackers**:
   - Put the Outbreaks Marker on “0” on the Outbreak Indicator.
   - Put the Infection Rate Marker on “2” (first space) on the Infection Rate Track.
   - Place 4 Cure Markers near the Cures Discovered Area.
5. **Separate Disease Cubes**:
   - Place them in four piles by color (Blue, Yellow, Black, Red).
6. **Epidemic Cards**: Pull out and set aside 6 Epidemic cards for now.
7. **Infection Draw Pile**: Shuffle the Infection cards (green back) and place them face down on the board to form the Infection Draw Pile.

### Infection Phase
1. **Draw Infection Cards**:
   - The Infector draws a number of Infection cards based on the Infection Rate.
2. - Each card drawn adds disease cubes to the pictured cities using matching colored cubes.
3. - If a city already has 3 cubes, an outbreak occurs (adding cubes to adjacent cities).
4. - Outbreaks continue if any new cubes would cause a city to exceed 3.

### Player Turn
1. **Actions**:
   - Each player gets 4 actions per turn.
2. **Available Actions**: 
   - Charter Flight: Move your pawn by playing the card corresponding to your current location.
   - Shuttle Flight: Move from any Research Station in your current city to another with a Research Station.
   - Direct Flight: Move to an adjacent city using a card from your hand.
   - Drive (or Ferry): Move to an adjacent city without a card.
   - Treat Disease: Remove one disease cube from the city you occupy, or all cubes if the Medic and in a cured disease city.
   - Discover A Cure: Requires 4 cards of the correct color for the Scientist; otherwise, needs 5. Place cure marker vial-side up when done.
   - Build Research Station: Use a card to build one at your current location.
   - Share Knowledge: Transfer a card from another player in the same city (unique ability: Researcher can give any card).
3. **Special Actions**:
   - Scientist: Discover cures with 4 cards of the correct color instead of 5.
   - Operations Expert: Build Research Station without playing a matching card.
   - Dispatcher: Move other players' pawns as if they were your own.

### Player Draw Phase
1. **Draw Cards**: After actions, draw 2 cards from the Player Draw Pile unless it’s an Epidemic card (discard and follow its instructions).

### Playing the Infector
1. **Epidemic**:
   - If there aren’t enough cubes to add, immediately end the game.
2. **Infection Rate**: Increase as per rules if drawing an Epidemic card.
3. **Draw Infection Cards**: Draw cards equal to the current Infection Rate and place them on the board.

### Winning Conditions
1. **Discover Cures**: 
   - Once all four cures are discovered (vial-side up), you win immediately.
2. **Defeat**:
   - If the Outbreaks Marker reaches 8 or if there aren’t enough cubes for Infection or drawing cards, the game ends in defeat.

### Strategy and Play
- Communicate effectively with your team to manage resources and outbreaks efficiently.
- Use special abilities wisely based on each role's unique strengths.
- Manage your hand size (7 cards) by discarding excess cards if needed.

Enjoy the challenge of working together as a disease-fighting team!
```

</details>
