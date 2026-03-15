---
game: wingspan
audience: expert
model: claude-opus-4
task: explain
---

# How to Play Wingspan

## Game Identity

Wingspan (Elizabeth Hargrave, Stonemaier Games, 2019) is a 1-5 player competitive engine-building game with a tableau-building core. Players construct asymmetric engines across three habitat rows on individual player mats, each row corresponding to one of three resource-generating actions. The game runs over 4 rounds with a diminishing action-cube economy (8/7/6/5 turns), creating escalating opportunity costs as engines mature. The 170-card bird deck provides enormous combinatorial variety, and scoring is a multi-axis optimization problem across six distinct point sources.

## Setup and Drafting

Each player receives 5 random bird cards, 5 food tokens (one per type), and 2 bonus cards. The opening draft is a constrained optimization: keep up to 5 birds, discarding 1 food per bird kept, then select 1 of 2 bonus cards. This initial resource allocation decision is consequential because it determines your early tempo and strategic direction. Aggressive bird retention (4-5 cards, 0-1 food) requires immediately productive food-generating turns, while conservative retention (1-2 cards, 3-4 food) allows faster bird deployment at the cost of fewer options.

The shared state consists of a 3-card face-up bird tray, a birdfeeder with 5 custom dice, a supply of food/egg tokens, and a goal board (competitive green or individual blue side) with 4 randomly placed double-sided goal tiles.

## Action Space

Each turn, a player commits one action cube to exactly one of four actions. The first three actions follow a unified pattern: place cube on leftmost exposed slot in the row, gain the slot's base benefit, then activate brown powers on that row's birds from right to left.

### Play a Bird

Place a bird from hand into the leftmost open slot of its matching habitat row. Cost structure: food tokens (shown on card) plus eggs (0/0/1/1/2 for columns 1-5). The wild food substitution rule (any 2 food tokens as 1 wild) provides flexibility at a 2:1 conversion rate. Birds with multiple habitat symbols offer placement flexibility. "When Played" powers resolve immediately. This is the only action that does not activate a row of existing birds.

### Gain Food (Forest)

Select dice from the birdfeeder to gain matching food tokens. The dual-food die face grants one token of either depicted type. Birdfeeder refresh triggers when all remaining dice show the same face or the tray is empty. Certain slots offer a card-to-food conversion (discard 1 card, gain 1 additional food from remaining dice). Brown forest birds then activate.

### Lay Eggs (Grassland)

Place eggs on any combination of birds, respecting per-bird egg limits. Certain slots offer a food-to-egg conversion. Brown grassland birds then activate. Eggs serve dual purpose: placement cost for columns 2-5 and 1 VP each at game end.

### Draw Cards (Wetland)

Draw from face-up tray or deck top. Face-up cards refill at end of turn, not immediately. Certain slots offer an egg-to-card conversion. Brown wetland birds then activate.

## Power Taxonomy

**When Played (white):** One-time effects on placement. Ranges from bonus card draws to extra bird plays to resource gains.

**When Activated (brown):** Recurring effects that fire on each row activation, resolved right-to-left. These are the primary engine components. Categories include:
- *Resource generators:* Gain food from supply, lay extra eggs, draw cards.
- *Predators:* Roll dice outside birdfeeder; on matching results, tuck a card from the deck (1 VP) and optionally cache food.
- *Flock builders:* Tuck cards from hand or deck behind the bird (1 VP per tucked card).
- *Cache builders:* Gain and cache food tokens on the bird (1 VP per cached food, non-spendable).
- *Interactive:* Some brown powers grant resources to all players (with the active player receiving a bonus), creating shared-benefit dynamics.

**Once Between Turns (pink):** Reactive powers triggered by opponents' actions (e.g., when another player plays a forest bird, gain 1 food from supply). Limited to one activation per interval between your turns.

## Round Economy and Goal Scoring

The diminishing cube count (one cube per round placed on the goal board) creates a tension: your engine becomes more powerful each round as more birds accumulate, but you have fewer actions to exploit it. This is the central design tension of Wingspan.

**Green (majority) goals:** Players rank by quantity of the targeted item. Ties split the sum of tied places' rewards, rounded down. Must have at least 1 qualifying item to score. Fourth and fifth place score 0.

**Blue (individual) goals:** 1 point per qualifying item, capped at 5. Lower variance, less interactive.

## Scoring Axes and Optimization

Final scoring sums six categories:

1. **Bird card face values** (printed VP, range 0-9; higher VP birds tend to have higher food costs)
2. **Bonus cards** (variable, condition-based; efficiency depends on card synergy with your tableau)
3. **End-of-round goals** (up to 4 scored goals; opportunity cost of the action cube must be weighed)
4. **Eggs on birds** (1 VP each; effectively a conversion of grassland actions into points)
5. **Cached food** (1 VP each; generated by specific bird powers)
6. **Tucked cards** (1 VP each; generated by predator and flock powers)

The optimization problem is multi-dimensional: maximizing one axis (e.g., eggs) means allocating actions away from others. High-level play involves reading which scoring axes are most efficient given your drawn birds, bonus cards, and the round goals.

## Strategic Framework

**Tempo:** Early rounds should prioritize deploying birds with strong brown powers in the rows you intend to use most frequently. Each bird played in Round 1 will activate far more often than one played in Round 4.

**Row specialization vs. diversification:** Deep investment in one row creates powerful chain activations but leaves you dependent on a single action type. Diversification provides flexibility for goal scoring and balanced resource access.

**Food economy:** The birdfeeder is a shared resource with imperfect information (dice rolls). The 2:1 wild conversion is a significant tempo loss and should be avoided through careful bird selection during drafting.

**Egg management:** Eggs transition from pure cost (columns 2-5) to pure VP in late game. The grassland row's egg-laying capacity should be calibrated against your bird placement needs.

**Card management:** The wetland row and card draw are your primary means of finding synergistic birds. Face-up card selection provides information advantage over blind deck draws but reveals your intentions to opponents.

**Pink power positioning:** In multiplayer games, pink powers generate value proportional to opponent count. In 4-5 player games, a well-placed pink power bird can generate substantial passive income.

**Goal awareness:** On the green (competitive) side, marginal investment to secure 1st or 2nd place in a round goal can be highly efficient. On blue, goals reward broad presence rather than concentrated effort.

Tiebreaker: unused food tokens. This rarely matters but slightly favors food-efficient play at the margins.
