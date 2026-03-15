---
game: century
model: claude-opus-4
task: fix_rules
---

ISSUES IDENTIFIED:
1. **Rulebook text ordering is disjointed**: The thematic flavor text (paragraphs about the spice trade) appears in the middle of the rules between the "Spice Cards" section and the "Upgrade Cards" section, breaking the flow of mechanical instructions. A reader encountering this mid-rules will lose track of the gameplay explanation.
2. **No explicit cube upgrade hierarchy in Setup**: The setup section (step 5) lists cube colors and their spice names but does not state that these represent an ascending value hierarchy (Yellow < Red < Green < Brown). The upgrade order is only revealed later when Upgrade Cards are explained. A new player reading setup instructions has no context for why the ordering matters.
3. **Upgrade Cards described only for "Upgrade 2"**: The rules explain how an "Upgrade 2" card works but never describe a general Upgrade card mechanic. It is unclear whether Upgrade cards with other numbers exist (e.g., "Upgrade 3") and how they would function. The rules should clarify that the number on an Upgrade card indicates how many single-level upgrades a player may perform.
4. **"Deck-building" terminology is misleading**: The Rest action description states this mechanism is called "deck-building," but Century uses a hand-management system, not a deck-building system. In deck-building games (e.g., Dominion), cards cycle through a draw pile and discard pile. In Century, played cards sit in front of you and return to hand on Rest. This mislabeling may confuse players familiar with the actual deck-building genre.
5. **Gold/silver token claiming rule is ambiguous**: The Claim section says "If you claim the leftmost or second leftmost Point card, take one gold or silver token from above that card." This phrasing suggests the player chooses between gold or silver. In reality, the leftmost card has gold tokens above it and the second card has silver tokens above it; you take from the pile that is physically above the card you claimed.
6. **Token sliding rule is incomplete**: The rule states "If you take the last gold token, slide the pile of silver tokens so it is now above the leftmost Point card." It does not address what happens when the silver tokens are also exhausted. It is unclear whether later claimants of the first two positions receive no bonus at all.
7. **Tiebreaker rule is counterintuitive and underspecified**: "The last player to take a turn wins the tie" is ambiguous. Since the game ends after the current round is completed, every player takes a turn in the final round. The rule likely means the player who sits latest in turn order (closest to the end of the round) wins, but this should be stated explicitly.
8. **No rule for empty Merchant or Point decks**: The rules describe sliding cards and drawing replacements when cards are acquired or claimed, but do not specify what happens if the Merchant or Point deck runs out of cards. The row may have fewer than 6 or 5 cards, and the rules are silent on this scenario.
9. **Starting cube distribution table placement**: The starting cube table (step 7) uses ordinal player positions (1st, 2nd, etc.) without clarifying that these correspond to clockwise seating from the first player, not to some other ordering.
10. **Caravan limit enforcement timing**: The rules state that caravan limit is checked "at the end of a player's turn," but it is not clear whether cubes gained from acquiring a Merchant card (cubes sitting on the acquired card transfer to your caravan) are subject to this limit check, or only cubes gained from playing cards.

SUGGESTED FIXES:
1. Move the thematic flavor text to the beginning of the rulebook as an introduction, before the Setup section, so it does not interrupt the mechanical rules.
2. Add an explicit statement in Setup step 5: "These colors represent an ascending value hierarchy: Yellow (lowest) -> Red -> Green -> Brown (highest). This order is used when upgrading cubes."
3. Generalize the Upgrade Cards description: "When playing an Upgrade card, you may perform a number of single-level upgrades equal to the number shown on the card. Each upgrade moves one cube up one level in the hierarchy (Yellow -> Red -> Green -> Brown). You are not required to use all available upgrades."
4. Replace the term "deck-building" with "hand management" or remove the parenthetical entirely. The Rest action recovers played cards to hand, which is a hand-management mechanism.
5. Rewrite the gold/silver token rule: "If you claim the leftmost Point card, take one gold token from the pile above it. If you claim the second leftmost Point card, take one silver token from the pile above it."
6. Add: "Once both the gold and silver token piles are exhausted, no bonus tokens are awarded for claiming the leftmost or second leftmost Point cards."
7. Rewrite the tiebreaker: "If there is a tie, the tied player who is latest in turn order (furthest clockwise from the first player) wins."
8. Add: "If the Merchant or Point deck is empty when a card needs to be drawn, simply slide existing cards to the left. The row may contain fewer cards than the starting number."
9. Add to step 7: "Player positions (1st through 5th) are determined by clockwise seating order starting from the first player."
10. Clarify: "The caravan limit of 10 cubes is checked at the end of your turn, regardless of how cubes were gained during that turn (from playing cards, acquiring cards with cubes on them, or any other source)."

CORRECTED RULES:

### Introduction
Centuries ago, the spice trade was the most important market in the world. It established and destroyed empires, compelled men to explore the far corners of the earth, and led to the discovery of new worlds. At that time, the value of spices even rivaled that of gold! As a caravan leader, your journey begins on the Spice Road.

### Game Setup
To set up a game of Century, follow these steps in order:

1. Shuffle the Point cards (orange back) to form a deck, then draw 5 cards and place them face up in a row to the left of that deck.
2. Place a pile of gold tokens equal to the number of players x2 above the first (leftmost) Point card. Then place a pile of silver tokens equal to the number of players x2 above the second Point card.
3. Among the Merchant cards (purple back), there are 10 cards with a purple border on the face-up side. These are the starting cards. Each player receives one "Create 2" card and one "Upgrade 2" card to form their starting hand. Return any remaining starting cards to the box.
4. Shuffle the remaining Merchant cards to form a deck. Draw 6 cards and place them face up in a row to the left of that deck.
5. Spices are represented by cubes. Separate them by color and place them into the bowls. The colors represent an ascending value hierarchy: Yellow/Turmeric (lowest) -> Red/Saffron -> Green/Cardamom -> Brown/Cinnamon (highest). This order is used when upgrading cubes.
6. Take a Caravan card (grey back) for each player in the game, being sure to include the card with the first player symbol. Shuffle them and deal one to each player. The player with the first player symbol on his Caravan card is the first player.
7. Place cubes on each player's Caravan card based on clockwise seating order from the first player:
   - 1st player: 3 yellow cubes
   - 2nd player: 4 yellow cubes
   - 3rd player: 4 yellow cubes
   - 4th player: 3 yellow cubes and 1 red cube
   - 5th player: 3 yellow cubes and 1 red cube

### Taking a Turn
Century is played over a series of rounds. Each player takes one turn per round, starting with the first player and going clockwise. On your turn, you must perform exactly 1 of the following actions:

- **Play**: Play a card from your hand.
- **Acquire**: Acquire a Merchant card from the market row.
- **Rest**: Take all previously played cards back into your hand.
- **Claim**: Claim a Point card.

### Play
Place a card from your hand face up in front of you and execute its effect. There are 3 types of Merchant cards:

**Spice Cards**: Take the number and color of cube(s) shown on the card from the supply bowls and place them on your caravan.

**Upgrade Cards**: Perform a number of single-level upgrades equal to the number shown on the card. Each upgrade moves one cube on your caravan up one level in the hierarchy (Yellow -> Red -> Green -> Brown). You are not required to use all available upgrades. For example, with an "Upgrade 2" card you may: upgrade two different yellow cubes to red, or upgrade one yellow cube to red and then upgrade that same red cube to green.

**Trade Cards**: Return the cube(s) shown above the arrow from your caravan to the supply bowls, then take the cube(s) shown below the arrow from the supply and place them on your caravan. A trade may be executed multiple times in a single play, as long as you have the required cubes each time.

### Acquire
To acquire a Merchant card, place one cube of any color from your caravan onto each Merchant card to the left of the card you wish to acquire, then take that card into your hand. The leftmost Merchant card costs nothing. Any cubes that were on the acquired card are placed onto your caravan. After acquiring, slide remaining cards to the left and draw a new card from the deck to fill the rightmost slot. If the deck is empty, the row simply has fewer cards.

### Rest
Take all cards you have previously played (face up in front of you) back into your hand. This is a hand-management mechanism that allows you to reuse your Merchant cards.

### Claim
To claim a Point card, you must have all cubes shown on that card in your caravan. Return those cubes to the supply bowls. Take the Point card and place it face down in front of you. Slide remaining Point cards to the left and draw a new card from the deck to fill the rightmost slot. If the deck is empty, the row simply has fewer cards.

If you claim the leftmost Point card, take one gold token from the pile above it. If you claim the second leftmost Point card, take one silver token from the pile above it. When the last gold token is taken, slide the silver token pile so it is above the leftmost Point card. Once all tokens of both types are exhausted, no further bonus tokens are awarded.

### Caravan Limit
A player's caravan can hold up to 10 cubes. At the end of your turn, if you have more than 10 cubes on your caravan (regardless of how they were gained), return cubes of your choice to the supply bowls until you have exactly 10.

### Cube Supply
The cube supply is considered unlimited. If a color runs out, use a suitable substitute.

### Game End
The game-end condition is triggered when any player claims their 5th Point card (or 6th in a 2-3 player game). Finish the current round so that all players have taken an equal number of turns. Then each player totals their score:
- Points printed on collected Point cards
- 3 points per gold token
- 1 point per silver token
- 1 point per non-yellow cube remaining on caravan

The player with the most points wins. In case of a tie, the tied player furthest clockwise from the first player (latest in turn order) wins.
