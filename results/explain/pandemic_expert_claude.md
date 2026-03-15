---
game: pandemic
audience: expert
model: claude-opus-4
task: explain
---

# Pandemic - Rules Explanation (Expert / Strategic Analysis)

## Game Identity

Pandemic (Matt Leacock, Z-Man Games) is a fully cooperative, deterministic-input/stochastic-output hand management and set collection game for 2-4 players. Play time is approximately 45 minutes. The game models infectious disease spread via an elegant "intensifying infection" mechanic that creates escalating tension through a non-random feedback loop.

## Core Mechanism: The Infection Ratchet

The central design innovation is the Epidemic resolution sequence. When an Epidemic card is drawn from the Player Draw Pile, three steps execute:

1. **Increase**: The Infection Rate Marker advances one position on the track (positions correspond to rates of 2, 2, 2, 3, 3, 4, 4).
2. **Infect**: The bottom card of the Infection Draw Pile is drawn, and 3 cubes are placed on the named city. If this would exceed the 3-cube-per-color limit, an outbreak triggers.
3. **Intensify**: The entire Infection Discard Pile is shuffled and placed on top of the remaining Infection Draw Pile.

The Intensify step is the key insight: it guarantees that cities which have already been infected will be drawn again in the near future. This creates a predictable threat landscape -- after an Epidemic, players know exactly which cities are at risk (those in the reshuffled discard pile), but not the order. This transforms the game from pure randomness into a probabilistic planning problem.

**Strategic implication**: After each Epidemic, the set of at-risk cities is fully known. The critical window is the number of Infection draws before the reshuffled cards cycle through. Cities with 2-3 cubes in the reshuffled set represent outbreak threats that must be triaged.

## Victory and Defeat Conditions

**Victory**: Discover cures for all four diseases. A cure is discovered by discarding 5 city cards of one color (4 for the Scientist) while at a Research Station. Victory is instant upon the fourth cure -- board state is irrelevant. Eradication is not required.

**Defeat** (any one triggers immediate loss):
- Outbreak counter reaches 8.
- Any disease cube color is depleted when placement is required.
- Player Draw Pile is exhausted when a player must draw.

The third condition functions as a hard timer. With 48 city cards in the Player deck minus starting hands and Epidemic cards, players have a finite number of turns before the deck runs out. This creates constant time pressure that intensifies as the game progresses.

## Turn Anatomy

Each turn proceeds through three mandatory phases:

### Phase 1: 4 Actions

Actions are selected freely from the following set, with repetition allowed:

**Movement**:
- **Drive/Ferry**: Move to an adjacent city. The adjacency graph wraps at board edges (e.g., Sydney-Los Angeles).
- **Direct Flight**: Discard a city card to teleport to that city. This is the primary card-consumption tension -- city cards are both transportation fuel and cure components.
- **Charter Flight**: Discard the card matching your current location to move anywhere. Useful but expensive, as it consumes a specific card.
- **Shuttle Flight**: Research-Station-to-Research-Station movement. No card cost. This makes station placement a strategic logistics decision.

**Special**:
- **Build a Research Station**: Discard the matching city card to place a station. Maximum 6 stations on the board; if all are placed, one must be relocated. The Operations Expert bypasses the card requirement.
- **Treat Disease**: Remove 1 cube from your current city. If the disease is cured, remove all cubes of that color for 1 action. The Medic removes all cubes of one color regardless of cure status.
- **Share Knowledge**: Transfer the card matching your shared city between co-located players. Both players must occupy the city named on the card. This constraint is the primary bottleneck for assembling cure sets. The Researcher can give any card, bypassing the city-matching restriction (but still receives under normal rules).
- **Discover a Cure**: At a Research Station, discard 5 same-color cards (4 for Scientist).

### Phase 2: Draw 2 Player Cards

Cards are drawn sequentially. Epidemic cards are resolved immediately upon draw and do not enter the hand. Hand limit is 7; excess must be discarded immediately (Special Event cards may be played instead).

**Special Event cards** can be played at any time, including other players' turns, at no action cost. Their timing flexibility makes them high-value assets for reactive play.

### Phase 3: Infect

Draw Infection cards equal to the current Infection Rate. Place 1 matching cube per card. Eradicated colors are ignored. A city receiving a 4th cube of one color triggers an outbreak.

## Outbreak Mechanics and Chain Reactions

When an outbreak occurs:
- No 4th cube is placed. Instead, 1 cube of the outbreaking color is added to each adjacent city.
- The Outbreaks Marker advances.
- If any adjacent city now exceeds 3 cubes of that color, a chain reaction outbreak occurs.
- **Critical rule**: Each city can only outbreak once per resolution sequence. This prevents infinite loops but does not prevent extensive chains across the network.

**Strategic note**: Chain reactions are the primary loss vector. The adjacency graph has several high-connectivity nodes (Istanbul, Cairo, Hong Kong, and others with 5+ connections) that function as outbreak amplifiers. Monitoring cube counts at these hubs is essential.

## Role Analysis

### Medic
Removes all cubes of one color per Treat action. After a cure is discovered, passively removes cubes of that color from any city entered or occupied (no action cost, triggers on all players' turns). The Medic is the strongest containment role and becomes extremely powerful once the first cure is found. Pair with the Scientist for an accelerated cure-then-clean strategy.

### Scientist
Discovers cures with only 4 cards. This reduces the set-collection threshold by 20%, which has cascading benefits: fewer cards consumed means more cards available for movement, and the cure can be assembled faster. The Scientist should be the primary cure discoverer and should be fed cards by other players.

### Researcher
Can give any card during Share Knowledge (not restricted to the current city's card). This dramatically increases card-transfer throughput and flexibility. The Researcher functions as a logistics hub -- other players should route to the Researcher to receive cards they need rather than orchestrating complex city-matching meetups.

### Operations Expert
Builds Research Stations without discarding a card. This enables rapid station network construction for Shuttle Flight logistics. The Operations Expert's value is in mobility infrastructure -- build stations at strategic crossroads to enable the entire team's movement economy.

### Dispatcher
Can move any player's pawn using standard movement actions, and can move any pawn to a city containing another pawn (1 action). The Dispatcher excels at orchestrating Share Knowledge meetings and positioning the Medic optimally. The ability to move other players to each other is extremely efficient for card transfers.

## Strategic Framework

### Card Economy
Every city card has dual use: movement or cure contribution. The fundamental strategic tension is deciding which cards to spend on travel and which to hoard for cures. Experienced players minimize Direct Flight usage and rely on Drive/Ferry, station networks, and the Dispatcher to preserve cards.

### Cure Priority
Prioritize curing the disease with the most cubes on the board or the one closest to causing cube depletion. The first cure is disproportionately valuable because it unlocks the Medic's passive ability and enhanced Treat Disease efficiency.

### Epidemic Timing
The number of Epidemics (4/5/6) is known before the game begins, and their approximate spacing can be estimated from pile sizes. After each Epidemic, the reshuffled discard pile defines the threat window. Count cards in the Infection Discard Pile to anticipate when the next Epidemic-reshuffled batch will cycle through.

### Outbreak Prevention
Treat cities at 3 cubes that are in the current Infection Discard Pile (and therefore about to re-enter the draw pile after the next Epidemic). Ignore 3-cube cities whose Infection cards are deep in the draw pile, as they are not immediate threats.

### Station Placement
Stations serve two functions: cure discovery locations and Shuttle Flight network nodes. Place stations to maximize connectivity for the team. Atlanta is guaranteed; additional stations should cover distinct geographic clusters to reduce transit times.

### Share Knowledge Optimization
The city-matching constraint on Share Knowledge makes card transfers the primary coordination challenge. Plan multi-turn sequences where two players converge on a target city to exchange the matching card. The Researcher and Dispatcher dramatically reduce this overhead.

## Edge Cases and Commonly Missed Rules

- A cured disease can still spread. Only eradicated diseases (cured + zero cubes on board) stop placing cubes.
- Charter Flight requires discarding the card of your **current** location, not the destination.
- The Dispatcher must use the card matching the moved pawn's current location for Charter Flights, not his own location.
- During an Epidemic, the bottom card is drawn (not the top) from the Infection Draw Pile.
- Hand limit enforcement is immediate upon exceeding 7 cards, not at end of turn.
- Special Event cards can be played during the discard-to-hand-limit process.
- Chain reaction outbreaks: each city outbreaks at most once, but cubes from multiple outbreaks can accumulate.
- If a Research Station must be built and all 6 are deployed, the active player chooses which existing station to relocate.
- In Normal/Heroic games, players may verbally describe their hands but may not show them. Both discard piles are public information at all times.
