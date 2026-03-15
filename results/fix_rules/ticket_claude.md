---
game: ticket
model: claude-opus-4
task: fix_rules
---

ISSUES IDENTIFIED:
1. Locomotive usage with gray routes is not explicitly addressed. The rules state Locomotives act as wild cards in "any set," and gray routes can be claimed with "a set of cards of any one color," but it is never clarified whether a player can use Locomotives alone (without any colored cards) to claim a gray route, or whether at least one non-Locomotive card is required to establish the color of the set.
2. The Longest Continuous Path scoring rule contains an ambiguous constraint: it says to count only "continuous lines of plastic trains of the same color." This could be misread as requiring all trains in the path to be the same player color (which they already are, since each player has one color), or it could be interpreted as requiring the route colors on the board to match. The intended meaning -- that the path must be a connected chain of that player's own train pieces -- is not stated with sufficient clarity.
3. The rules never define how "Longest Continuous Path" length is measured. It is unclear whether length is counted by the number of train cars (individual spaces occupied) or by the number of routes claimed. This distinction matters because routes vary in length from 1 to 6.
4. The component list states 240 Colored Train Cars with "45 each in Blue, Red, Green, Yellow and Black," but 45 times 5 equals 225, not 240. The extra 15 are described as "extra replacement cars in each color," but the rules never clarify that replacement cars are not used during gameplay or how many extras exist per color. This creates confusion about whether a player actually plays with 45 or 48 trains.
5. The rules use the term "set of the same type" when describing route claiming, but Train Car cards are described both by type names (Box, Passenger, Tanker, etc.) and by colors (Purple, Blue, Orange, etc.). The relationship between card type and card color is never explicitly stated. A player might wonder whether "Passenger" cards are always blue or whether type and color are independent attributes.
6. The initial Destination Ticket draw requires keeping at least 2 of 3 cards, but mid-game draws require keeping at least 1 of 3. This asymmetry is correct by design but is easy to overlook because the two rules appear in different sections with no cross-reference or explicit note about the difference.
7. The face-up Locomotive replacement rule has an edge case gap. The rules say if after drawing one card the replacement is a Locomotive, the player cannot take it. But they do not clarify what happens if the replacement causes three or more Locomotives to appear face-up. The three-Locomotive reset rule is stated separately, but the interaction and timing between the two rules is not sequenced.
8. The game-end trigger says the final round begins when a player has "0, 1 or 2 trains left at the end of his turn," but the rules never address what happens if a player wants to claim a route but does not have enough trains to fill all spaces. It is unspecified whether a player must have enough trains to fully cover a route before claiming it.
9. The first-player rule ("the most experienced traveler goes first") is entirely subjective and provides no objective tiebreaker or alternative method for determining who starts.
10. The rules never specify what happens if the Destination Ticket deck is completely empty when a player chooses to draw Destination Tickets. It only addresses the case where "less than 3" remain.

SUGGESTED FIXES:
1. Add a clarification under the Claiming Routes or Train Car Cards section: "Locomotives may be used as part of any set. When claiming a gray route, a player may use Locomotives together with colored cards of one type, or may use Locomotives alone without any colored cards."
2. Rewrite the Longest Continuous Path paragraph to: "When evaluating path length, trace a connected sequence of routes claimed by that player. The path must be continuous -- each route in the path must share a city endpoint with the next route. A path may pass through the same city more than once, but each individual train car (board space) may only be counted once."
3. Add an explicit definition: "Path length is measured by counting the total number of individual train car spaces occupied along the continuous path, not the number of routes."
4. Clarify the component note: "Each player uses exactly 45 trains during the game. The additional replacement cars included in the box are spares for lost or damaged pieces and are not used in normal play."
5. Add a sentence bridging type and color: "Each of the 8 Train Car card types corresponds to one color: Box (purple), Passenger (blue), Tanker (orange), Reefer (white), Freight (green), Hopper (yellow), Coal (black), and Caboose (red). When claiming a route, play cards matching the route's color."
6. Add a parenthetical reminder during the mid-game Destination Ticket draw: "He must keep at least one of them (note: this differs from initial setup, where players must keep at least two)."
7. Clarify the Locomotive replacement timing: "After any card is drawn or replaced from the face-up display, immediately check whether three or more of the five face-up cards are Locomotives. If so, discard all five face-up cards and deal five new replacements before the player continues drawing."
8. Add a rule: "A player may only claim a route if he has enough train cars remaining to place one on every space of that route. A player cannot partially claim a route."
9. Replace the subjective first-player rule with: "The most experienced traveler goes first. If players cannot agree, the youngest player goes first (or use any mutually agreed random method)."
10. Add: "If the Destination Ticket deck is empty, a player may not choose the Draw Destination Tickets action."

CORRECTED RULES:

### Train Car Cards (corrected)

There are 8 types of regular Train Car cards, plus Locomotive cards. Each type corresponds to a color used on the board's routes: Box (purple), Passenger (blue), Tanker (orange), Reefer (white), Freight (green), Hopper (yellow), Coal (black), and Caboose (red).

Locomotives are multi-colored and act as a wild card that can be part of any set of cards when claiming a route. A player may also use Locomotives alone, without any colored cards, to claim a route (including gray routes).

If a Locomotive card is one of the five face-up cards, the player who draws it may only draw one card instead of two. If, after having drawn one card, the replacement card turned face-up is a Locomotive, the player cannot take it. After any card is drawn or replaced, immediately check whether three or more of the five face-up cards are Locomotives. If so, discard all five face-up cards and turn five new cards face-up from the deck. Repeat this check until fewer than three Locomotives are face-up.

If a player draws a Locomotive from the top of the deck as a blind draw, it still counts as a single card, and the player may still draw a total of two cards that turn.

A player may have any number of cards in his hand at any time.

When the deck is exhausted, shuffle the discard pile to form a new draw deck. Shuffle thoroughly, as cards tend to be discarded in same-color groups.

If both the draw deck and discard pile are empty, a player cannot choose the Draw Train Car Cards action. He may only claim a route or draw Destination Tickets.

### Claiming Routes (corrected)

To claim a route, a player must play a set of cards equal to the number of spaces in that route. A set must consist of cards of the same color. Most routes require cards matching a specific color (e.g., a blue route requires blue Passenger Car cards). Gray routes can be claimed using a set of any single color. Locomotives may substitute for any color in a set and may be used alone.

A player may only claim a route if he has enough plastic train cars to place one on every space. A player cannot partially claim a route.

When a route is claimed, the player places one of his plastic trains on each space of the route and discards all cards used. He then advances his Scoring Marker along the Scoring Track according to the Route Scoring Table.

A player may claim any open route on the board. He is never required to connect to previously claimed routes. A player may claim at most one route per turn.

Some cities are connected by Double-Routes. A single player cannot claim both routes between the same two cities. In 2- or 3-player games, only one of the two Double-Routes may be claimed; once one player claims either route, the other route is closed for the remainder of the game.

### Drawing Destination Ticket Cards (corrected)

A player may use his turn to draw additional Destination Ticket cards. He draws 3 cards from the top of the Destination Ticket deck. He must keep at least 1 (note: during initial setup, the minimum is 2). He may keep 2 or all 3 if he wishes. Any returned cards are placed on the bottom of the deck.

If fewer than 3 Destination Tickets remain in the deck, the player draws only those available. If the Destination Ticket deck is empty, a player may not choose this action.

Each Destination Ticket shows two cities and a point value. If the player has a continuous chain of his claimed routes connecting those two cities at game end, the point value is added to his score. If not, the point value is subtracted.

Destination Tickets are kept secret from other players until final scoring. A player may hold any number of Destination Tickets.

### Game End (corrected)

When any player's stock of plastic train cars is reduced to 0, 1, or 2 at the end of his turn, each player (including that player) gets exactly one more turn. The game then ends.

### Calculating Scores (corrected)

Verify each player's route points by recounting claimed routes against the Route Scoring Table.

Reveal all Destination Tickets. Add the point value of each completed ticket (where the two cities are connected by a continuous chain of that player's routes). Subtract the point value of each incomplete ticket.

Determine the Longest Continuous Path for each player. Path length is measured by counting the total number of individual train car spaces along a connected sequence of that player's claimed routes. A continuous path may loop and pass through the same city multiple times, but each individual train car space may be counted only once. The player with the longest path receives the bonus card and adds 10 points to his score. If multiple players tie for the longest path, all tied players receive the 10-point bonus.

The player with the most points wins. If tied, the player who completed the most Destination Tickets wins. If still tied, the player with the Longest Continuous Path wins.
