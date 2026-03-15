---
game: century
audience: expert
model: claude-opus-4
task: explain
---

# Century: Spice Road - Expert Rules Analysis

## Game Classification and Core Mechanisms

Century: Spice Road (Emerson Matsuuchi, Plan B Games, 2017) is a lightweight engine-building game for 2-5 players. The core mechanisms are hand management, deck-building (in the literal sense of constructing a hand of reusable cards), commodity conversion, and market row acquisition with positional cost. The game belongs to the same design lineage as Splendor, using a constrained action space (one of four actions per turn) combined with resource conversion toward set-collection goals.

## Setup and Asymmetric Starting Conditions

Setup follows a standard market-row pattern for both merchant cards (6 visible) and point cards (5 visible). Bonus token pools (gold above position 1, silver above position 2) scale at 2 per player.

The starting resource distribution introduces deliberate asymmetry:

| Player position | Starting cubes |
|---|---|
| 1st | 3 yellow |
| 2nd | 4 yellow |
| 3rd | 4 yellow |
| 4th | 3 yellow + 1 red |
| 5th | 3 yellow + 1 red |

This compensates for turn-order advantage. Later players receive either more total cubes or higher-value cubes. Notably, the 4th/5th players' single red cube is worth one upgrade step, which has a tempo value slightly exceeding one yellow cube, providing a meaningful offset to the positional disadvantage of acting later in each round.

## Action Space Analysis

Each turn consists of exactly one of four mutually exclusive actions.

### Play

Three subtypes exist:

**Spice (production) cards**: Pure resource generation. These are the entry point of the conversion pipeline, producing cubes from the supply. Their value is measured in cube-turns (total production over the course of a game, factoring in rest frequency).

**Upgrade cards**: Each upgrade step promotes one cube one level along the Yellow-Red-Green-Brown chain. An "Upgrade N" card grants N discrete steps that may target any combination of cubes. Crucially, you may use fewer than N steps -- partial use is explicitly permitted. This means an "Upgrade 2" can function as "Upgrade 1" when that is all that is needed, which is an important flexibility consideration when evaluating card acquisitions.

**Trade cards**: Perform a fixed exchange at a defined ratio. The critical rule interaction is that a single play of a trade card allows **unlimited repetitions** of the same trade in that action, constrained only by available cubes. This makes high-ratio trade cards significantly more powerful than they appear, since a card trading 2 yellow for 1 green effectively converts 6 yellow to 3 green in one action, provided you have the cubes. This multiplier effect is central to efficient engine design.

### Acquire

The positional cost mechanism (place one cube of any color on each card to the left of your target) creates a dynamic market with three interacting subsystems:

1. **Positional pricing**: Cards further right are more expensive. The leftmost card is always free.
2. **Cube accumulation on cards**: Cubes deposited as payment become part of the acquired card's value for the next acquirer. This creates a prisoner's-dilemma dynamic: passing on a cube-laden card gives your opponent a windfall.
3. **Cube color is irrelevant for payment**: Any cube pays for any position, meaning yellow cubes (zero end-game value) are the optimal payment currency when available.

After acquisition, the row slides left and refills from the deck. Timing acquisitions around this slide can matter: acquiring a card shifts everything leftward, making previously expensive cards cheaper for the next player.

### Rest

Picking up all played cards is the only recovery mechanism. This creates a fundamental tension: the more cards in your engine, the more potential output per cycle, but rest actions represent pure tempo loss. Optimal play minimizes rest frequency while maximizing output per cycle. The "cycle length" (number of actions between rests) is a key efficiency metric.

### Claim

Fulfilling a point card requires exact cube matching (return the depicted cubes to supply). The position-based bonus token system (gold = 3 VP at position 1, silver = 1 VP at position 2) adds a spatial priority element to the point card market. When the gold pile is exhausted, the silver pile shifts to position 1, meaning the bonus potential degrades over the course of the game.

The slide-and-refill mechanic after claiming means the point card market is somewhat unpredictable. Players cannot plan more than one or two claims ahead without risk of the target card shifting or being taken.

## Resource Economy and Conversion Efficiency

The spice hierarchy (Yellow < Red < Green < Brown) defines the conversion economy. Key efficiency considerations:

- **Upgrade efficiency**: Each upgrade step adds approximately 1 VP equivalent of cube value (since non-yellow cubes are worth 1 VP at end-game). However, the real value of upgrades is fulfilling point card requirements, where the VP-per-cube ratio on high-value cards far exceeds 1.
- **Trade card evaluation**: A trade card's value depends on (a) the ratio of output value to input value, (b) the repeatability benefit, and (c) pipeline compatibility with other held cards.
- **Cube velocity**: The rate at which cubes enter your caravan, get converted, and get spent on point cards determines overall engine throughput.

## Caravan Limit (10 Cubes)

The 10-cube caravan limit is a hard cap checked at end of turn. Excess cubes must be discarded (player's choice). This constraint primarily affects production-heavy strategies and creates a timing pressure: you must convert or spend cubes before your caravan overflows. It also makes high-value production cards (those generating many cubes at once) slightly less valuable if your pipeline cannot process the throughput within the caravan limit.

## Game End Trigger and Scoring

The endgame trigger is asymmetric by player count:
- **4-5 players**: 5th point card claimed
- **2-3 players**: 6th point card claimed

The round completes after the trigger, ensuring equal turns. This means the triggering player may not have the advantage -- opponents get one final turn to claim a point card or optimize their caravan.

**Scoring components:**
- Point card face values (primary scoring axis)
- Gold tokens: 3 VP each
- Silver tokens: 1 VP each
- Non-yellow cubes on caravan: 1 VP each (minor but can decide close games)

**Tiebreaker**: Later turn order wins. This subtly favors players who act later in the round, which partially compounds their starting-resource compensation.

## Strategic Considerations

1. **Engine compactness vs. power**: A smaller hand cycles faster (fewer rest actions), but a larger hand produces more per cycle. Finding the right hand size (typically 5-8 cards including starters) is a central strategic decision.
2. **Acquisition timing**: Early game favors acquiring cards to build the engine. A common mistake is claiming point cards too early before the engine is efficient.
3. **Gold token racing**: The 3 VP gold bonus is significant. Two gold tokens (6 VP) can swing a game. Players should track whether racing for position-1 point cards is viable.
4. **Cube payment optimization**: When acquiring, always pay with yellow cubes if possible, since they have zero end-game value.
5. **Endgame timing**: Triggering the endgame is advantageous when you are ahead, but the round-completion rule means opponents get a response turn. Consider whether opponents can close a scoring gap in one action.
6. **Market denial**: Acquiring a card an opponent needs, or claiming a point card they are building toward, provides indirect interaction in an otherwise low-interaction game.

## Edge Cases and Clarifications

- Trade card repetition: each repetition within a single play is mandatory in full (you cannot do a partial trade on any individual repetition).
- Upgrade partial use: explicitly allowed. You may upgrade 0, 1, or 2 cubes with an "Upgrade 2" card.
- Cube supply is unlimited by rule. Component shortage is handled by substitution.
- The leftmost merchant card is always free to acquire (no cubes placed).
- Cubes placed on merchant cards during acquisition are not returned to supply -- they transfer to the next acquirer of that card.
- Yellow cubes on your caravan at game end score nothing. Only red, green, and brown cubes score 1 VP each.
