---
game: cascadia
model: claude-opus-4
task: fix_rules
---

ISSUES IDENTIFIED:

1. **Tile count table is garbled/unreadable.** The setup section (lines for 2, 3, and 4 players) shows tile counts but the player count labels are missing from the extracted text. The original reads ": 43 (or remove 42)", ": 63 (or remove 22)", ": 83 (or remove 2)" without clearly stating which line is for 2, 3, or 4 players.

2. **Game end trigger is ambiguous regarding turn completion.** The rules state "If, at the end of any player's turn, there are no face-down Habitat Tiles left in the stacks to replace the one taken, the game ends immediately." This is unclear about whether all players get equal turns. The parenthetical note says each player plays exactly 20 turns, but the trigger mechanism could cause the game to end mid-round if tiles run out during a non-last player's turn.

3. **Overpopulation resolution order is unclear when cascading.** When 4 identical tokens appear, they are automatically wiped and replaced. The rules note "this could happen multiple times on any given player's turn." However, there is no explicit instruction about what happens if, after replacing the 4 tokens, the new draw produces 3 of the same -- does the active player then get the optional choice to wipe those 3? The interaction between the automatic 4-of-a-kind wipe and the optional 3-of-a-kind wipe during cascading is not fully specified.

4. **Nature Token spending timing is inconsistent.** Page 6 says "you may optionally spend a Nature Token" before selecting a combination, and page 8 says "On your turn, before you select a tile and token, you may spend a Nature Token." However, the rules do not clarify whether you can spend Nature Tokens after resolving overpopulation but before selecting, or whether the Nature Token spend happens before the overpopulation check.

5. **No explicit rule about what happens when the Cloth Bag runs out of tokens.** The rules explain replacing Wildlife Tokens from the bag but never address the scenario where the bag is empty when a replacement token is needed.

6. **Keystone Tile definition is incomplete.** The rules mention Keystone Tiles and show that placing a matching wildlife on one earns a Nature Token, but they never explicitly define what makes a tile a "Keystone Tile" beyond the visual indicator. The component list says "85 Habitat Tiles including 25 Keystone Tiles" but the distinguishing characteristic (single wildlife icon) is only implied, not stated.

7. **Habitat corridor scoring for dual-terrain tiles is ambiguous.** Tiles can have one or two terrain types. The rules say tiles are included in a corridor "if they share at least one matching edge." For dual-terrain tiles, it is unclear whether the entire tile counts toward the corridor of each habitat type it contains, or only the portion/edge that matches. Do both halves of a dual-terrain tile count as separate members of their respective corridors?

8. **Elk scoring Card D ("circular formation") is undefined.** The rules say groups must be in a "circular formation, as pictured" but the text-only rulebook does not define what a circular formation means in hexagonal geometry (e.g., a ring of 6 hexes around a center? A loop of any size?).

9. **Hawk line-of-sight definition is incomplete.** The rules state a line of sight is "a straight line from flat side to flat side of the hexagons" and is "only interrupted by the presence of another hawk." It does not clarify: (a) whether the line of sight requires tiles to exist along the path or can cross empty spaces, (b) whether the line of sight extends infinitely or has a maximum range, (c) whether non-hawk wildlife tokens or empty tiles block line of sight.

10. **Fox Card B and D reference "unique animal pairs" without defining "pair."** The rules say foxes score based on "unique animal pairs directly adjacent to it" and that "pairs of other animals do not need to be adjacent to each other." The term "pair" is ambiguous -- does it mean two tokens of the same species, or does it mean two tokens considered together regardless of species? The clarification helps but the base definition is missing.

11. **Bear adjacency restriction lacks precision.** The rules say "two groups may not be placed next to one another" for bears. It is unclear whether this means no bear from one scoring group can be adjacent to any bear from another scoring group, or whether bears that are adjacent simply cannot both score. What happens to bears that are adjacent to multiple groups?

12. **Salmon "run" triangle exception is confusing.** The rules state: "a group of 3 salmon in a triangle shape may count as a run, but no other salmon may be attached to this run." This contradicts the general run definition (each salmon adjacent to no more than two other salmon), since in a triangle each salmon is adjacent to exactly two others. The exception phrasing suggests the triangle is a special edge case but does not explain why it needs special mention.

13. **Starter Habitat Tile properties are never described.** The rules mention distributing Starter Habitat Tiles but never describe what habitats or wildlife icons they contain, whether they have special properties, or whether they are double-sided.

14. **Solo mode setup references "a 2-player game" setup but adjustments are vague.** The solo rules say "Follow the setup for a 2-player game with the following exceptions" but only mention giving yourself one Starter Habitat Tile and placing stacks to the left. It does not restate the tile count (43 tiles) or confirm that Nature Tokens, scoring cards, and other setup steps remain the same.

15. **Tiebreaker for habitat corridor majorities with more than 2 players is complex and potentially ambiguous.** The 3/4-player majority rules describe several tie scenarios but do not address all possible cases, such as: what if in a 4-player game, two players tie for largest and two players tie for second largest?

16. **The "exactly 20 turns" note appears to be a derived fact, not a rule.** The rules state players play exactly 20 turns in parenthetical notes, but this depends on the correct tile count being used. If the tile count is wrong (due to the garbled table), players could play a different number of turns. This should be stated as a verification check, not an assumed fact.

17. **No rule about the order of tile and token placement.** The rules say "you will place them into your environment in any order" but do not clarify whether this means you can place the token first (on a pre-existing tile) and then the tile, or whether there are any restrictions on this ordering that could affect strategy.

18. **Family/Intermediate variant scoring card details are missing.** The Family Variant Scoring Card is referenced and a brief description is given (score points for groups of same wildlife by size), but the actual point values per group size are not provided in the text.


SUGGESTED FIXES:

1. **Fix tile count table.** Reformat as:
   - 2 players: 43 tiles (or remove 42 from the full set of 85)
   - 3 players: 63 tiles (or remove 22 from the full set of 85)
   - 4 players: 83 tiles (or remove 2 from the full set of 85)

2. **Clarify game end and equal turns.** Add: "The game ends at the conclusion of the round in which the last Habitat Tile is drawn from the stacks. All players must have an equal number of turns. If the stacks run out during a round, remaining players in that round still complete their turns using only the tiles and tokens remaining in the display."

3. **Clarify overpopulation cascading.** Add: "After resolving an automatic 4-of-a-kind wipe, check the new set of tokens again. If 4 of the same appear again, repeat the automatic wipe. If 3 of the same appear after any automatic wipe, the active player may choose to wipe them as per the 3-of-a-kind rule. All overpopulation checks must be fully resolved before the active player selects a combination."

4. **Clarify Nature Token timing.** Rewrite the turn sequence as: "(1) Check and resolve overpopulation. (2) Optionally spend Nature Token(s). (3) Select a Habitat Tile + Wildlife Token combination. (4) Place tile and token. (5) Replace tile and token in the display."

5. **Add Cloth Bag empty rule.** Add: "If the Cloth Bag is empty when a Wildlife Token needs to be drawn, leave that display slot without a Wildlife Token. Players may still select the unpaired Habitat Tile but receive no Wildlife Token with it."

6. **Define Keystone Tiles explicitly.** Add: "Keystone Tiles are Habitat Tiles that display only a single wildlife icon (rather than two or three). They are identifiable by [visual indicator, e.g., a special border or symbol]. There are 25 Keystone Tiles among the 85 Habitat Tiles."

7. **Clarify dual-terrain tile corridor scoring.** Add: "Each Habitat Tile counts toward the corridor of every habitat type shown on that tile. For dual-terrain tiles, the tile is a member of both habitat corridors simultaneously, provided the matching edge connects to another tile of the same habitat type."

8. **Define Elk Card D circular formation.** Add: "A circular formation consists of a closed loop of elk where each elk in the loop is adjacent to exactly two other elk in the same formation, forming a ring. The minimum circular formation is a triangle of 3 elk."

9. **Clarify Hawk line of sight.** Add: "A line of sight extends in a straight line across any number of hexagonal tiles (including tiles without wildlife tokens and empty spaces where no tile exists) in any of the six directions defined by flat-side-to-flat-side adjacency. Line of sight is only blocked by another hawk token. Non-hawk wildlife tokens do not block line of sight."

10. **Define "animal pair" for Fox scoring.** Add: "An 'animal pair' means two tokens of the same non-fox wildlife species. For Fox Cards B and D, count how many different non-fox species have at least two tokens in the fox's adjacent spaces. The two tokens of a pair do not need to be adjacent to each other, only both adjacent to the fox (or fox pair)."

11. **Clarify Bear group adjacency restriction.** Add: "No bear that is part of a scoring group may be adjacent to any bear that is part of a different scoring group. Bears that violate this adjacency restriction cause both adjacent groups to not score. Single bears that are not part of any scoring group do not count as a 'group' for this restriction."

12. **Clarify Salmon triangle run.** Rewrite: "A run is a group of adjacent salmon forming a line or chain, where each salmon is adjacent to at most two other salmon in the run, and no salmon outside the run is adjacent to any salmon in the run. A triangle of 3 salmon (where each is adjacent to the other two) is a valid run, but because every edge is occupied, no additional salmon may be adjacent to any salmon in this triangle."

13. **Describe Starter Habitat Tiles.** Add: "Each Starter Habitat Tile is a triple-hex tile showing three different habitat types and three wildlife icons. Starter Habitat Tiles are double-sided; players use whichever side is face-up when distributed."

14. **Clarify Solo mode setup.** Add: "Solo mode uses 43 Habitat Tiles (the same count as a 2-player game). All other setup steps (scoring cards, Nature Tokens, initial display of 4 tiles and 4 tokens) remain the same as the standard game."

15. **Complete tiebreaker scenarios.** Add for 3/4-player games: "If two players tie for largest, they receive 2 points each. Any remaining players who tie for the next largest receive 0 points each (since there is no second-largest bonus when two players already share the largest). If all players tie, each receives 1 point."

16. **Reframe the 20-turn note as a verification.** Change to: "If setup was performed correctly, each player should play exactly 20 turns. If the game ends sooner or later, verify that the correct number of tiles was used during setup."

17. **Confirm tile/token placement order freedom.** Add: "You may place the tile and token in either order. For example, you may place the Wildlife Token on an existing tile in your environment first, then place the new Habitat Tile, or vice versa."

18. **Include Family/Intermediate scoring values.** Add the point values from the Family Variant Scoring Card (group of 1 = X points, group of 2 = Y points, etc.) or reference that they are printed on the card itself.


CORRECTED RULES:

### Setup -- Tile Count Table (Corrected)

Using the chart below, determine how many Habitat Tiles you need based on the number of players. Randomly select these tiles without looking at them.

| Players | Tiles to Use | Tiles to Remove |
|---------|-------------|-----------------|
| 2       | 43          | 42              |
| 3       | 63          | 22              |
| 4       | 83          | 2               |

(Note: This is 20 per player, plus 3.)

### Turn Summary (Corrected and Clarified)

At the beginning of each turn, there will be four Habitat Tiles and four Wildlife Tokens in the center of the play area, arranged in four distinct combinations (each with one Habitat Tile and one Wildlife Token).

**Step 1 -- Resolve Overpopulation:**
Before you make a selection, check the four Wildlife Tokens for overpopulation:
- If all 4 tokens are the same type, they are **automatically** wiped. Set all 4 aside, then draw 4 new tokens one at a time from the Cloth Bag, pairing each with a Habitat Tile in order. Check again -- this automatic wipe can happen multiple times.
- If exactly 3 tokens are the same type (and the 4th is different), the active player **may choose** to wipe those 3 tokens. Set the 3 aside, then draw 3 new tokens one at a time from the Cloth Bag, pairing each with a Habitat Tile in order. You may only do this once per turn.
- After all overpopulation is resolved, return any wiped tokens to the Cloth Bag.

**Step 2 -- Optionally Spend Nature Tokens:**
Before selecting your combination, you may spend one or more Nature Tokens (returning them to the supply) to do one of the following per token spent:
1. Take ANY one of the four Habitat Tiles and ANY one of the four Wildlife Tokens (they do not need to be a paired combination).
2. Wipe ANY number of Wildlife Tokens and replace them (following the same replacement process as overpopulation).

If you do not spend a Nature Token, you must take one of the four existing paired combinations.

**Step 3 -- Place the Habitat Tile:**
Place the selected Habitat Tile into your environment following these rules:
- A. It must be placed adjacent to at least one tile already in your environment (sharing at least one edge).
- B. It may not be placed on top of another tile, and no existing tiles may be moved.
- Note: Matching terrain types is not required for placement but may earn points during final scoring.

**Step 4 -- Place the Wildlife Token:**
Place the selected Wildlife Token onto any single Habitat Tile in your environment following these rules:
- A. The target tile must not already have a Wildlife Token on it.
- B. The target tile must display the matching wildlife type among its icons.
- You may place the token on the tile you just placed this turn, or on any other eligible tile.
- If no legal placement exists, or if you choose not to place the token, return it to the Cloth Bag.
- If you place the token onto a Keystone Tile (a tile with only one wildlife icon), take a Nature Token from the supply.

You may place the tile and token in either order.

**Step 5 -- Replenish the Display:**
Replace the taken Habitat Tile by drawing from the top of any face-down stack. Replace the taken Wildlife Token by drawing one randomly from the Cloth Bag. Do not rearrange existing tiles and tokens in the display; simply fill the empty positions. If the Cloth Bag is empty, leave the token position vacant.

Your turn is complete. Play passes clockwise.

### End Game and Scoring (Corrected)

The game ends when, at the end of any player's turn, there are no face-down Habitat Tiles remaining in the stacks to replace the one taken. All players in the current round complete their turns so that everyone has played an equal number of turns (20 turns each if setup was performed correctly).

**Scoring Step 2 -- Habitat Tile Corridors (Clarified):**
For each player, score 1 point per Habitat Tile in their largest contiguous habitat corridor for each of the 5 habitat types. A corridor is a group of connected tiles sharing at least one edge of matching habitat type. Dual-terrain tiles count toward the corridor of each habitat type they display, provided the matching edges connect.

**Scoring Step 3 -- Habitat Tile Corridor Majorities (Clarified):**

*2-player game:* 2-point bonus to the player with the largest corridor in each habitat type. If tied, 1 point each. No bonus for second largest.

*3/4-player game:* 3-point bonus to the player with the largest corridor in each habitat type. 1-point bonus for second largest.
- If 2 players tie for largest: 2 points each; no points for next largest.
- If 3 or 4 players tie for largest: 1 point each; no points for next largest.
- If 2 or more players tie for second largest: 0 points each.

*Solo game:* 2-point bonus for each habitat type where your largest corridor is 7 or more tiles.

### Hawk Line of Sight (Clarified)

A line of sight is a straight line extending from one hawk through the flat-side-to-flat-side direction of the hexagonal grid, continuing across any number of tiles (occupied or empty) until it reaches another hawk. Only the presence of an intervening hawk blocks a line of sight. Non-hawk wildlife tokens, empty tiles, and gaps in the tile layout do not block line of sight. Tiles do not need to be physically present along the path for line of sight to exist.

### Bear Group Adjacency (Clarified)

Bear scoring groups may not be adjacent to one another. This means that no bear belonging to one scoring group may be hexagonally adjacent to any bear belonging to a different scoring group. If this adjacency restriction is violated, neither group scores. Lone bears (not part of any scoring group) do not trigger this restriction. When evaluating bear groups, choose the interpretation that maximizes your score.

### Salmon Run Definition (Clarified)

A run of salmon is a group of adjacent salmon tokens forming a chain, where each salmon in the run is adjacent to at most two other salmon within that run. No salmon outside the run may be adjacent to any salmon within the run. A triangle formation of exactly 3 salmon (each adjacent to the other two) qualifies as a valid run; however, because all adjacent positions along the triangle's edges are occupied by run members, no additional salmon may be attached to this triangular run.
