---
game: cascadia
audience: expert
model: claude-opus-4
task: explain
---

# Cascadia: Expert-Level Rules Analysis

## Game Identity and Design Space

Cascadia is a competitive tile-laying and token-drafting game for 1-4 players by Randy Flynn (Flatout Games / AEG, 2021). It occupies a distinctive design niche: a spatial optimization puzzle with dual-layer scoring (habitat geography and wildlife pattern-matching) mediated by a constrained drafting mechanism. The game's depth emerges from the tension between these two scoring axes, since optimal tile placement for habitat corridors frequently conflicts with optimal token placement for wildlife scoring cards.

## Components and Their Mechanical Significance

- **85 Habitat Tiles** (including 25 Keystone Tiles): hexagonal tiles bearing one or two terrain types (Mountains, Forests, Prairies, Wetlands, Rivers) and one to three wildlife icons indicating which tokens may be legally placed on them. The distribution of single-terrain vs. dual-terrain tiles, and the wildlife icon combinations printed on them, define the solution space for both scoring axes.
- **25 Keystone Tiles**: a critical subset of the habitat tiles. Each Keystone Tile displays a single terrain type and a single wildlife icon. Placing the matching wildlife token on a Keystone Tile yields a Nature Token. These tiles are the primary engine for Nature Token generation.
- **100 Wildlife Tokens** (20 each of Bear, Elk, Salmon, Hawk, Fox): drawn from a cloth bag, these are placed onto habitat tiles to score against the active Wildlife Scoring Cards.
- **5 Starter Habitat Tiles**: each is a three-hex tile providing the initial environment seed. Each starter tile comes pre-printed with terrain and wildlife icons, establishing initial placement constraints.
- **21 Wildlife Scoring Cards** (4 per species + 1 Family/Intermediate): these define the specific pattern-matching objectives for each wildlife species in any given game. The card combination selected during setup is the single largest source of strategic variance between sessions.
- **25 Nature Tokens**: the game's sole flexible currency, usable for drafting flexibility or worth 1 VP each if unspent at game end.

## Setup Protocol

1. Determine tile count by player count: 2P uses 43 tiles, 3P uses 63 tiles, 4P uses 83 tiles (formula: 20 per player + 3). This guarantees exactly 20 turns per player.
2. Shuffle tiles face-down into stacks. Excluded tiles return to the box unseen -- this introduces hidden information about which tiles and terrain/wildlife combinations are unavailable.
3. Select one Wildlife Scoring Card per species (5 total) and display publicly. The "A" set is recommended for introductory games; experienced players should randomize.
4. Distribute one Starter Habitat Tile per player randomly. Return unused starters to the box.
5. Reveal 4 Habitat Tiles face-up and draw 4 Wildlife Tokens from the bag, pairing them left-to-right into 4 tile-token combinations.
6. Place Nature Tokens in a common supply.
7. First player: whoever most recently saw one of the five wildlife species in real life (or random selection).

**Setup Implications**: The random card combination and tile exclusion mean that each session presents a unique optimization landscape. Experienced players should immediately assess the selected scoring cards and identify which wildlife share habitat tile icons (resource competition) and which scoring patterns create spatial conflicts.

## Turn Structure (Detailed)

Each turn follows a strict sequence:

### Phase 1: Overpopulation Check

Before the active player selects, check the 4 Wildlife Tokens in the display:

- **4 identical tokens**: mandatory wipe. Remove all 4, draw 4 replacements one at a time from the bag, pairing each sequentially with the corresponding tile. This can cascade -- if the 4 replacements are again identical, wipe again.
- **3 identical tokens**: the active player may optionally wipe those 3 (not the fourth). Draw 3 replacements, pair sequentially. This optional wipe may only be performed once per turn, and occurs before any Nature Token expenditure.

**Edge case**: The mandatory 4-of-a-kind wipe can trigger multiple times on a single turn. The optional 3-of-a-kind wipe is limited to once per turn. The ordering matters: resolve all mandatory wipes first, then the active player decides whether to exercise the optional wipe.

### Phase 2: Selection (with optional Nature Token expenditure)

The active player selects one tile-token combination from the display. By default, the tile and token must come from the same paired slot. However, before selecting, the player may spend Nature Token(s) for one of two effects:

1. **Decouple selection**: take any one of the 4 tiles and any one of the 4 tokens, regardless of pairing.
2. **Selective wipe**: wipe any number of Wildlife Tokens (not tiles) and replace them from the bag, following the same sequential replacement process as overpopulation.

There is no limit to the number of Nature Tokens spent per turn. Multiple Nature Tokens can be spent for multiple effects (e.g., wipe tokens, then decouple selection). If the player has zero Nature Tokens, they must take an existing paired combination. Spent Nature Tokens return to the common supply.

**Strategic note**: The Nature Token spend is the game's primary agency-expansion mechanism. Spending a token for decoupling is often correct when the optimal tile and optimal token are in different slots. However, each token spent is -1 VP at endgame, so the expected point gain from the improved draft must exceed 1 point.

### Phase 3: Placement

The selected tile and token are placed into the player's environment in any order.

**Tile placement rules**:
- Must be adjacent to at least one existing tile (sharing a hex edge).
- Cannot be placed on top of another tile. No tile rearrangement is permitted.
- Terrain matching is not required for legal placement -- but terrain adjacency directly affects habitat corridor scoring.

**Token placement rules**:
- Must be placed on a tile that (a) does not already have a token and (b) displays the matching wildlife icon.
- The token may be placed on the tile just drafted or on any qualifying tile already in the environment.
- If no legal placement exists (or the player chooses not to place), the token returns to the bag.
- If the token is placed on a Keystone Tile (matching the Keystone's single wildlife icon), the player gains a Nature Token from the supply.

**Edge cases**:
- Placement order matters: if you place the tile first, the token can go onto it (if the tile supports that wildlife). If you place the token first onto an existing tile, the new tile remains empty. Sequencing is a micro-decision.
- A player may always choose not to place a wildlife token, returning it to the bag. This is occasionally correct when placing the token would damage a wildlife scoring pattern (e.g., breaking bear group separation rules or attaching an unwanted salmon to a run).

### Phase 4: Replenishment

Replace the taken tile from the top of any face-down stack. Replace the taken token by drawing one from the bag. Existing display items do not shift -- the new tile and token fill the vacated slot, maintaining positional pairing.

Play passes clockwise.

## Game End Trigger

The game ends immediately when a player takes a tile and there are no face-down tiles remaining to replace it. Because the tile count formula guarantees exactly 20 turns per player, all players will have taken exactly 20 turns (the last player to act is the one who takes the final tile from the stacks, and that turn completes normally without replacement).

## Scoring System (Four Categories)

### 1. Wildlife Scoring Cards

Each of the five wildlife species scores according to its active scoring card. The card combinations create the primary strategic puzzle. The four-tier system (A-D) per species generates 4^5 = 1,024 possible scoring card combinations, ensuring significant replayability. Below is a detailed analysis of each species' scoring family:

**Bears**: score for isolated groups of specific sizes. Critical constraint across all bear cards: no two bear groups may be adjacent to each other. Group adjacency is measured token-to-token via shared tile edges.
- (A) Pairs: escalating points for total number of pairs (4/11/19/27 for 1/2/3/4 pairs).
- (B) Exactly 3: 10 points per group of exactly 3. Groups of other sizes score nothing. Binary scoring creates a high-risk, high-reward dynamic.
- (C) Groups of 1, 2, or 3: individual scoring per group size with a 3-point bonus for having at least one of each size. Encourages diversified group sizes.
- (D) Groups of 2, 3, or 4: larger groups required, broader than B but lower ceiling per group.

**Edge case**: Two bear groups are considered adjacent if any bear in one group occupies a tile sharing an edge with a tile containing a bear from another group. A single bear token that is adjacent to two separate groups would invalidate both groups' separation requirement. Buffer zones of at least one tile-width must be maintained between all bear groups.

**Elk**: score for groups in specific spatial formations. Unlike bears, elk groups may be adjacent to one another, but each elk token scores for exactly one group.
- (A) Straight lines: connected flat-side-to-flat-side in a single hex direction. Points escalate by line length. Orientation is critical -- all elk in a line must follow the same hex axis.
- (B) Specific shapes: exact hex formations as pictured on the card, in any orientation.
- (C) Contiguous groups of any shape: escalating points by size. The most forgiving elk card.
- (D) Circular formations as pictured.

**Scoring ambiguity resolution**: when elk groups are connected and could be partitioned multiple ways, always choose the interpretation yielding the maximum points. This is a combinatorial optimization sub-problem that rewards careful analysis during scoring.

**Salmon**: score for runs (chains). A run is defined as a group of adjacent salmon where each salmon is adjacent to at most 2 other salmon within the run. No salmon outside the run may be adjacent to any salmon in the run.
- (A) Points per run by size, up to a maximum scoring size of 7.
- (B) Points per run by size, up to a maximum scoring size of 5.
- (C) Points per run by size, only sizes 3-5 score. Runs of 1-2 are worthless.
- (D) One point per salmon in the run plus one point per adjacent non-salmon wildlife token (type does not matter). This is the most interaction-dependent salmon card, rewarding dense placement near other wildlife.

**Critical edge case**: a triangle of 3 salmon (each adjacent to exactly 2 others) is a legal run -- the only case where a non-linear configuration is legal. However, no fourth salmon may be adjacent to any salmon in this triangle. Any configuration where a salmon is adjacent to 3 or more other salmon breaks the run definition entirely.

**Hawks**: score for spatial distribution and line-of-sight mechanics.
- (A) Escalating points for each hawk not adjacent to any other hawk. Pure dispersion scoring.
- (B) Each hawk must be non-adjacent to all other hawks AND have a direct line of sight to at least one other hawk. Line of sight follows a straight hex-axis direction (flat-side to flat-side) and is blocked only by intervening hawks.
- (C) 3 points per line of sight between any two hawks. A single hawk can participate in multiple lines of sight. Maximizing this requires careful geometric placement along shared hex axes.
- (D) Pair hawks; escalating points per pair based on unique non-hawk wildlife types on tiles between them. Each hawk may only be part of one pair.

**Line-of-sight definition**: a straight line along one of the three hex axes, from flat edge to flat edge, with no limit on distance. The line is blocked only by another hawk -- empty tiles, tiles with other wildlife, and tiles without any wildlife do not block line of sight. Only hawks interrupt the line.

**Foxes**: score for adjacency diversity around each fox (the 6 surrounding hexes for a single fox, up to 8 for a fox pair in Card D).
- (A) Escalating points per fox based on number of unique wildlife types (including other foxes) directly adjacent. Maximum: 5 unique types.
- (B) Escalating points per fox based on number of unique wildlife pairs adjacent (excluding fox pairs). Paired animals need not be adjacent to each other, only both individually adjacent to the fox.
- (C) Escalating points per fox based on the count of the most abundant single non-fox wildlife type adjacent. Rewards clustering same-species neighbors around a fox.
- (D) Score per fox pair based on unique wildlife pairs adjacent to the combined adjacency zone. Paired animals need not be adjacent to each other.

### 2. Habitat Tile Corridors

For each of the 5 terrain types, each player scores 1 point per tile in their largest contiguous corridor of that terrain. Contiguity requires sharing a matching terrain edge -- on dual-terrain tiles, only the edges displaying the relevant terrain type count for that corridor. A single dual-terrain tile can belong to two different corridors simultaneously (one for each terrain type), making dual-terrain tiles highly efficient for corridor scoring.

Only the largest corridor per terrain type scores. Fragmented corridors are entirely wasted from a base-scoring perspective. This winner-take-all mechanic within each player's environment demands committed corridor planning.

### 3. Habitat Corridor Majorities

Bonus points are awarded to the player(s) with the largest corridor in each terrain type, creating the game's primary player-interaction scoring dimension. Scoring varies by player count:

- **Solo**: 2-point bonus for any terrain corridor of 7+ tiles.
- **2 players**: 2 points for largest; if tied, 1 point each. No points for second largest.
- **3-4 players**: 3 points for largest, 1 point for second largest. Tie-breaking: if 2 tie for largest, 2 points each, 0 for next. If 3+ tie for largest, 1 point each, 0 for next. Any tie for second largest yields 0 each.

This majority system creates a 3-point swing in 3-4 player games between first place and no bonus, making corridor investment in contested terrains a high-stakes decision.

### 4. Nature Tokens

Each unspent Nature Token is worth 1 VP. Given that competitive scores typically range 80-100, each token represents roughly 1% of a final score.

### Tiebreaker

Most Nature Tokens remaining. If still tied, shared victory.

## Strategic Framework

### Macro-Strategy: Card-Driven Planning

The five Wildlife Scoring Cards selected during setup should dictate the entire game plan. Before the first draft, assess:

1. **Wildlife-habitat icon overlap**: which wildlife share tile icons? If Bear and Fox both appear frequently on Mountain/Prairie tiles, those two objectives compete for placement slots.
2. **Spatial compatibility**: do the active scoring patterns require clustering (e.g., Bear C requiring groups of 1, 2, and 3) or dispersion (e.g., Hawk A requiring isolation)? Conflicting spatial demands on the same habitat region create tension.
3. **Keystone tile priority**: identify which Keystone Tiles generate the most value. A Keystone Tile whose wildlife matches a high-scoring pattern is doubly valuable (Nature Token + wildlife score contribution).

### Drafting Heuristics

- **Tile quality is generally more permanent than token quality**: a tile locks a terrain edge configuration forever. A token merely occupies a slot. Prioritize tiles that serve both corridor and wildlife placement needs.
- **Nature Token ROI**: spending a Nature Token must yield more than 1 point of expected value. Common high-value spends include decoupling to claim a tile critical for corridor majority, or wiping to find a specific wildlife token for a high-value pattern completion.
- **Denial drafting**: in 2-player games especially, monitor the opponent's corridor sizes. Taking a tile that blocks their majority can be a 2-point swing (they lose 2, you potentially gain 2). In 3-4 player games, denial is less targeted but still relevant when corridors are close.

### Tile Placement Principles

- **Corridor contiguity**: always consider whether a tile extends a corridor or fragments it. Dual-terrain tiles are particularly valuable as corridor bridges, connecting otherwise disjoint groups of the same terrain.
- **Wildlife slot preservation**: avoid placing tiles that create dead zones -- positions where no wildlife token can be usefully placed because the available icons on surrounding tiles are already filled or irrelevant to active scoring cards.
- **Edge geometry**: in the early game, prefer placements that maximize future adjacency options (convex frontier with many open edges). In the late game, fill interior gaps that complete corridors or provide adjacency for fox scoring.

### Wildlife Pattern Optimization

- **Bears**: plan group locations early. The non-adjacency constraint means that bear groups must be separated by at least one tile-width of buffer. Map out bear "zones" before committing. On cards B and D, exact group size matters -- an extra bear in a group can void its scoring entirely.
- **Elk (line cards A and B)**: straight-line and shaped formations require deliberate hex-axis planning. Prioritize tiles that extend these lines. Note that orientation matters for lines -- all elk in a line must follow a single flat-side-to-flat-side direction.
- **Salmon**: runs are fragile. A single misplaced salmon adjacent to an existing run can invalidate it by violating the isolation constraint. Protect run endpoints by not placing salmon-compatible tiles adjacent to them, or by filling those adjacent tiles with non-salmon tokens.
- **Hawks**: line-of-sight scoring (cards B and C) rewards deliberate hex-axis alignment across large distances. Place hawks on tiles that share hex-axis lines with future hawk placements. The non-adjacency requirement for cards A and B means hawks should be spaced at least 2 tiles apart.
- **Foxes**: maximize adjacency diversity by placing foxes in high-traffic areas surrounded by varied wildlife. Fox placement should typically come after neighboring tokens are established, making foxes a mid-to-late game priority.

### Nature Token Economy

Nature Tokens function as both a currency and a scoring element. The decision to spend versus save is the game's central economic tension:

- Early-game Keystone completions are high-value because the Nature Tokens generated have more turns of potential utility remaining.
- Late-game Nature Token spending is lower-cost because fewer turns remain where the token's optionality has value.
- Aim to spend tokens during the mid-game when the marginal point gain from improved drafts is highest, and conserve the last 1-2 tokens for endgame VP.
- A player who completes all available Keystone Tiles in their environment has a significant economic advantage. Prioritize Keystone completion when the wildlife token aligns with scoring needs.

### Overpopulation as Strategic Information

The overpopulation mechanism is not merely a variance-reduction tool. The optional 3-of-a-kind wipe is a free action (no Nature Token cost) that can reshape the token display. Strategically:

- If 3 tokens match and you do not need any of them, wipe to introduce fresh options at no cost.
- If 3 tokens match and one of the remaining options is ideal for you but also desirable for opponents, consider whether wiping improves or worsens your position.
- The mandatory 4-of-a-kind wipe can cascade, introducing significant variance. On average, this favors the active player who gets first pick of the refreshed display.
- Wiped tokens are set aside during resolution and returned to the bag only after all overpopulation checks complete. This subtly affects draw probabilities for replacement tokens.

## Rule Interactions and Subtle Points

1. **Token return to bag**: when a player cannot or chooses not to place a wildlife token, it returns to the bag -- not removed from the game. This maintains the overall token distribution and affects future draw probabilities.
2. **Display refill ordering**: new tiles and tokens fill the exact slot vacated by the selection. Existing display items do not shift. This means the positional pairing of remaining items is preserved for subsequent players.
3. **Dual-terrain corridor counting**: a tile with Mountains/Forest terrain contributes its Mountain edges to a Mountain corridor and its Forest edges to a Forest corridor simultaneously. It can be part of the largest corridor for both terrain types.
4. **Starter tile integration**: the Starter Habitat Tile is a three-hex tile that functions identically to placed tiles for all purposes -- corridor scoring, wildlife placement, adjacency. It is part of the environment from turn 1.
5. **Nature Token supply limit**: there is no stated per-player cap on Nature Tokens. The supply of 25 is the practical ceiling. In rare cases, multiple players competing for Keystone completions can deplete the supply.
6. **Exact turn count**: every player takes exactly 20 turns regardless of player count. This is guaranteed by the tile count formula (20n + 3, where n is player count, minus the 3 tiles in the initial display that get replaced during gameplay) and the end-game trigger.
7. **Keystone Token timing**: the Nature Token is gained immediately upon placing a wildlife token on a Keystone Tile during Phase 3. Since Nature Token spending occurs in Phase 2 (before selection and placement), a Nature Token gained from Keystone placement is available starting on the player's next turn.
8. **Placement order within a turn**: the rules state the tile and token may be placed "in any order." This is a genuine choice: placing the token first (on a pre-existing tile) leaves the newly drafted tile empty, which can be relevant for Keystone timing or corridor extension decisions.

## Variants (Summary)

- **Family Variant**: uses a single shared Wildlife Scoring Card where points are based on contiguous group sizes of any wildlife. Majority scoring is optional. Significantly reduces cognitive load.
- **Intermediate Variant**: same as Family but with differentiated group-size scoring thresholds.
- **Solo Mode**: uses the 2-player tile count (43 tiles). After selecting a tile-token pair, the pair furthest from the draw stacks is discarded (removed from the game entirely), and remaining pairs slide away from the stacks before refilling. This discard-and-slide mechanic creates an additional tempo pressure absent from multiplayer. Solo majority scoring: 2-point bonus for any corridor of 7+. Scores are benchmarked against a rating chart (60+ "A good start" through 110+ "Ascended").
- **Achievements / Scenarios**: a 15-scenario meta-progression system with escalating difficulty, specific card combinations, and multi-objective challenges. Provides structured long-term goals.
- **Rule Restrictions**: 10 variant constraints for experienced play, including mandatory terrain matching on placement, display reduced to 3 pairs, double Nature Token cost for actions, and prohibition on placing wildlife tokens on the tile just drafted. These restrictions fundamentally alter the strategic calculus and are recommended for groups seeking deeper challenge.
