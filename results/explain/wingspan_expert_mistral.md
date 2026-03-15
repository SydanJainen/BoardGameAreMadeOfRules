---
model: mistral-nemo:12b
temperature: 0.8
timestamp: '2026-02-18T14:12:17.926697Z'
execution_time_seconds: 50.02
prompt_length: 24550
model_alias: mistral
tokens: 1213
---

# Rule Explanation for Expert Audience

**Wingspan Expert Rules Analysis**

**Game Overview:**
Wingspan is a competitive bird-collection, engine-building game for 1-5 players designed by Elizabeth Hargrave. Players are bird enthusiasts seeking to attract the best birds to their aviary while gaining food tokens via custom dice, laying eggs using marbled egg miniatures, and expanding their bird collection by drawing from hundreds of unique bird cards.

**Components:**

1. **Bird Cards (170)**: Shuffled into a deck, placed on the bird tray (3 face-up). Each card has habitat, food cost, egg limit, nest type, wingspan, and powers.
   - *Habitat*: Forest, grassland, wetland (each with 5 slots).
   - *Food Cost*: Invertebrate, seed, fish, fruit, rodent; wild can use any.
   - *Egg Limit*: Varies per bird.
   - *Nest Type*: Platform, bowl, cavity, ground; star nests are wild.
   - *Wingspan*: Used for comparison in some powers.
   - *Powers*: WHEN ACTIVATED (brown), BIRD POWER, ONCE BETWEEN TURNS (pink), WHEN PLAYED (no color).

2. **Food Tokens (103)**: Five types; public information. Cached food tokens worth 1 VP at game end.

3. **Egg Tokens (75)**: Six colors; laid on bird cards, discarded when used. Excess eggs lost.

4. **Action Cubes (40)**: Eight per player; placed on mat actions, moved left each turn, refilled at round end.

5. **Birdfeeder Dice Tower**: Five food dice; refilled when empty or if all show the same face.

6. **Bonus Cards (26)**: Scored at game end. Players start with 1, gain more from birds.

7. **Goal Board**: Four goals per round; green side has spaces for 1st-3rd place, blue side scores 1 point per targeted item (max 5 points).

8. **First Player Token**: Passed clockwise each round.

**Setup:**

- Shuffle bird cards into a deck, place 3 face-up on the tray.
- Place food and egg tokens in supplies.
- Toss food dice into the birdfeeder tower.
- Choose goal board side (green or blue).
- Shuffle goal tiles without looking at them; place one on each of four blank spaces.
- Players receive a mat, action cubes, bonus cards, bird cards, and food tokens.

**Player Setup:**

1. Keep up to 5 bird cards; discard others based on food tokens kept.
2. Choose 1 bonus card to keep.
3. Randomly select the first player.

**Turn Structure:**
Each turn, players place an action cube on their mat's action spots (play a bird, gain food, lay eggs, draw cards) and move it left each turn until it reaches the end of its row.

**Actions:**

1. **Play a Bird**:
   - Pay food cost using tokens cached on birds or from supply.
   - Place bird card in habitat slot; activate WHEN PLAYED power if present.
   - Limit: Max 5 birds per habitat.

2. **Gain Food**:
   - Select dice from the birdfeeder tower to gain food tokens.
   - Gain an additional food token by discarding one bird card (optional).
   - Activate brown powers on forest birds from right to left.

3. **Lay Eggs**:
   - Lay eggs on birds according to their egg limit.
   - Gain bonus food-to-egg conversion using one food token (optional).
   - Activate brown powers on grassland birds from right to left.

4. **Draw Bird Cards**:
   - Draw cards from face-up tray or deck based on action cube slot.
   - Gain additional card by discarding one egg (optional).
   - Activate brown powers on wetland birds from right to left.

**Round Structure:**

1. All players place all their action cubes.
2. Score end-of-round goal using the goal board.
3. Discard face-up bird cards; replenish tray with new cards.
4. Rotate first player token clockwise.
5. Players have fewer actions each round (8 in Round 1, 5 in Round 4).

**Game End and Scoring:**
At game end, score points for:

- Bird cards
- Bonus cards
- End-of-round goals
- Eggs on bird cards
- Cached food tokens
- Tucked bird cards

The player with the most points wins; ties broken by unused food tokens.

**Edge Cases & Rule Interactions:**

1. **Food Tokens**: There's no limit to food tokens players can have or in the supply.
2. **Egg Tokens**: Excess eggs beyond a bird's egg limit are lost.
3. **Birdfeeder Dice Tower**: If all dice show the same face, throw them back into the tower before gaining food.
4. **Goal Board**: Green side majority scoring has ties resolved by adding scores and dividing by tied players (round down).
5. **Bonus Cards**: Scored at game end; players start with 1 card and gain more from birds.

**Strategic Considerations:**

- Balance bird habitats to optimize end-of-round goals.
- Leverage brown powers for food, eggs, or cards.
- Use pink powers on opponents' turns strategically.
- Cache food tokens for bonus points at game end.
- Tuck birds under flocking birds for added bonuses.

**Designer Notes:**

- Food types are generalized; wild icons can use any type of food.
- Egg limits are scaled down from real-life bird egg-laying habits.
- Wingspan is used for bird comparison in some abilities.

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
**Wingspan Expert Rules Analysis**

**Game Overview:**
Wingspan is a competitive bird-collection, engine-building game for 1-5 players designed by Elizabeth Hargrave. Players are bird enthusiasts seeking to attract the best birds to their aviary while gaining food tokens via custom dice, laying eggs using marbled egg miniatures, and expanding their bird collection by drawing from hundreds of unique bird cards.

**Components:**

1. **Bird Cards (170)**: Shuffled into a deck, placed on the bird tray (3 face-up). Each card has habitat, food cost, egg limit, nest type, wingspan, and powers.
   - *Habitat*: Forest, grassland, wetland (each with 5 slots).
   - *Food Cost*: Invertebrate, seed, fish, fruit, rodent; wild can use any.
   - *Egg Limit*: Varies per bird.
   - *Nest Type*: Platform, bowl, cavity, ground; star nests are wild.
   - *Wingspan*: Used for comparison in some powers.
   - *Powers*: WHEN ACTIVATED (brown), BIRD POWER, ONCE BETWEEN TURNS (pink), WHEN PLAYED (no color).

2. **Food Tokens (103)**: Five types; public information. Cached food tokens worth 1 VP at game end.

3. **Egg Tokens (75)**: Six colors; laid on bird cards, discarded when used. Excess eggs lost.

4. **Action Cubes (40)**: Eight per player; placed on mat actions, moved left each turn, refilled at round end.

5. **Birdfeeder Dice Tower**: Five food dice; refilled when empty or if all show the same face.

6. **Bonus Cards (26)**: Scored at game end. Players start with 1, gain more from birds.

7. **Goal Board**: Four goals per round; green side has spaces for 1st-3rd place, blue side scores 1 point per targeted item (max 5 points).

8. **First Player Token**: Passed clockwise each round.

**Setup:**

- Shuffle bird cards into a deck, place 3 face-up on the tray.
- Place food and egg tokens in supplies.
- Toss food dice into the birdfeeder tower.
- Choose goal board side (green or blue).
- Shuffle goal tiles without looking at them; place one on each of four blank spaces.
- Players receive a mat, action cubes, bonus cards, bird cards, and food tokens.

**Player Setup:**

1. Keep up to 5 bird cards; discard others based on food tokens kept.
2. Choose 1 bonus card to keep.
3. Randomly select the first player.

**Turn Structure:**
Each turn, players place an action cube on their mat's action spots (play a bird, gain food, lay eggs, draw cards) and move it left each turn until it reaches the end of its row.

**Actions:**

1. **Play a Bird**:
   - Pay food cost using tokens cached on birds or from supply.
   - Place bird card in habitat slot; activate WHEN PLAYED power if present.
   - Limit: Max 5 birds per habitat.

2. **Gain Food**:
   - Select dice from the birdfeeder tower to gain food tokens.
   - Gain an additional food token by discarding one bird card (optional).
   - Activate brown powers on forest birds from right to left.

3. **Lay Eggs**:
   - Lay eggs on birds according to their egg limit.
   - Gain bonus food-to-egg conversion using one food token (optional).
   - Activate brown powers on grassland birds from right to left.

4. **Draw Bird Cards**:
   - Draw cards from face-up tray or deck based on action cube slot.
   - Gain additional card by discarding one egg (optional).
   - Activate brown powers on wetland birds from right to left.

**Round Structure:**

1. All players place all their action cubes.
2. Score end-of-round goal using the goal board.
3. Discard face-up bird cards; replenish tray with new cards.
4. Rotate first player token clockwise.
5. Players have fewer actions each round (8 in Round 1, 5 in Round 4).

**Game End and Scoring:**
At game end, score points for:

- Bird cards
- Bonus cards
- End-of-round goals
- Eggs on bird cards
- Cached food tokens
- Tucked bird cards

The player with the most points wins; ties broken by unused food tokens.

**Edge Cases & Rule Interactions:**

1. **Food Tokens**: There's no limit to food tokens players can have or in the supply.
2. **Egg Tokens**: Excess eggs beyond a bird's egg limit are lost.
3. **Birdfeeder Dice Tower**: If all dice show the same face, throw them back into the tower before gaining food.
4. **Goal Board**: Green side majority scoring has ties resolved by adding scores and dividing by tied players (round down).
5. **Bonus Cards**: Scored at game end; players start with 1 card and gain more from birds.

**Strategic Considerations:**

- Balance bird habitats to optimize end-of-round goals.
- Leverage brown powers for food, eggs, or cards.
- Use pink powers on opponents' turns strategically.
- Cache food tokens for bonus points at game end.
- Tuck birds under flocking birds for added bonuses.

**Designer Notes:**

- Food types are generalized; wild icons can use any type of food.
- Egg limits are scaled down from real-life bird egg-laying habits.
- Wingspan is used for bird comparison in some abilities.
```

</details>
