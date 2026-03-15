---
model: mistral-nemo:12b
temperature: 0.8
timestamp: '2026-02-18T13:55:55.349649Z'
execution_time_seconds: 35.16
prompt_length: 7812
model_alias: mistral
tokens: 931
---

# Rule Explanation for Expert Audience

**Century: Spice Road - Expert Level Analysis**

**Setup:**

1. **Point Deck (A, B):** Shuffle orange-backed Point cards; draw 5, place face up left of deck. Initially, these cards represent goals to achieve during the game.
   - *Strategic Consideration:* Keep track of upcoming Point cards for planning future turns.

2. **Gold/Silver Tokens (C, D):** Place piles equal to 2x number of players above respective cards. These are used to acquire Point cards and end-game scoring.
   - *Edge Case:* If gold tokens run out, slide silver pile to leftmost Point card.

3. **Merchant Deck (E, F):** Shuffle purple-backed Merchant cards; draw 6, place face up left of deck. These represent actions players can perform during the game.
   - *Rule Interaction:* Acquiring a Merchant card fills empty slot and draws new card from deck.

4. **Spice Bowls (G):** Separate colored cubes (yellow, red, green, brown) and place in bowls according to shown order. These are used for trading and achieving Point cards.
   - *Edge Case:* If cube supply runs out, use substitute material.

5. **Caravan Cards (H, I):** Deal one grey-backed Caravan card per player; first player starts with marked symbol. Place yellow and red cubes on each card as indicated in the table.
   - *Strategic Consideration:* Monitor opponents' caravans to anticipate their moves.

**Gameplay:**

Players take turns clockwise, performing one action:

1. **Play:** Play a Merchant card from hand; effects are Spice, Upgrade, or Trade cards.
   - **Spice Cards:** Take indicated cubes from bowls and place on caravan.
     + *Strategic Consideration:* Balance acquiring useful cubes vs. leaving favorable trades for opponents.
   - **Upgrade Cards (x2):** May upgrade two cubes one level each. Upgrade priority: yellow → red → green → brown.
     + *Edge Case:* You can upgrade the same cube twice, e.g., yellow → red → green.
   - **Trade Cards:** Return indicated cubes to bowls and take specified cubes from supply to caravan.
     + *Rule Interaction:* Trade any number of times in a row with available cubes.

2. **Acquire:** Pay for Merchant card by placing ANY cube on each preceding card, then take acquired card into hand.
   - *Strategic Consideration:* Acquire cards that synergize with your current collection or upcoming Point cards.

3. **Rest:** Take all played face-up cards back into hand to build Merchant deck.
   - *Edge Case:* You cannot Rest if you didn't play any cards this turn.

4. **Claim:** Collect indicated cubes from caravan, return them to bowls, take Point card face down, and place gold/silver tokens as needed.
   - *Rule Interaction:* Sliding Point cards fills empty slot and draws new card from deck.

**Endgame:**

- Game ends after fifth Point card is claimed (sixth in 2-3 player games).
- Score points: Point cards + Gold/Silver tokens + Non-yellow cubes on caravan. Gold = 3 points, Silver = 1 point, Other cubes = 1 point each.
- Tiebreaker: Last player to take a turn wins.

**Strategic Considerations:**

- Balance cube acquisition and trading for maximum efficiency.
- Prioritize Point cards that offer more valuable rewards (e.g., gold tokens).
- Monitor opponents' caravans to anticipate their moves and block potential Point cards.
- Build your Merchant deck strategically, acquiring cards that complement each other's effects.

**Expert Tips:**

1. Focus on yellow cubes early for trading flexibility.
2. Prioritize high-value trades over small ones.
3. Keep track of upcoming Point cards and plan accordingly.
4. Pay attention to opponents' Merchant decks; acquired cards can reveal their intentions.
5. Consider claiming multiple Point cards in one turn when possible to deny opponents valuable rewards.

**Edge Cases & Interactions:**

- Trading cubes beyond what's needed for a trade wastes resources, so be mindful of cube limits and supply availability.
- When acquiring a card with cubes on it, those cubes go directly onto your caravan without occupying any spaces.
- If you claim the leftmost or second-leftmost Point card without taking gold/silver tokens, don't slide piles as there are no empty slots to fill.

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
**Century: Spice Road - Expert Level Analysis**

**Setup:**

1. **Point Deck (A, B):** Shuffle orange-backed Point cards; draw 5, place face up left of deck. Initially, these cards represent goals to achieve during the game.
   - *Strategic Consideration:* Keep track of upcoming Point cards for planning future turns.

2. **Gold/Silver Tokens (C, D):** Place piles equal to 2x number of players above respective cards. These are used to acquire Point cards and end-game scoring.
   - *Edge Case:* If gold tokens run out, slide silver pile to leftmost Point card.

3. **Merchant Deck (E, F):** Shuffle purple-backed Merchant cards; draw 6, place face up left of deck. These represent actions players can perform during the game.
   - *Rule Interaction:* Acquiring a Merchant card fills empty slot and draws new card from deck.

4. **Spice Bowls (G):** Separate colored cubes (yellow, red, green, brown) and place in bowls according to shown order. These are used for trading and achieving Point cards.
   - *Edge Case:* If cube supply runs out, use substitute material.

5. **Caravan Cards (H, I):** Deal one grey-backed Caravan card per player; first player starts with marked symbol. Place yellow and red cubes on each card as indicated in the table.
   - *Strategic Consideration:* Monitor opponents' caravans to anticipate their moves.

**Gameplay:**

Players take turns clockwise, performing one action:

1. **Play:** Play a Merchant card from hand; effects are Spice, Upgrade, or Trade cards.
   - **Spice Cards:** Take indicated cubes from bowls and place on caravan.
     + *Strategic Consideration:* Balance acquiring useful cubes vs. leaving favorable trades for opponents.
   - **Upgrade Cards (x2):** May upgrade two cubes one level each. Upgrade priority: yellow → red → green → brown.
     + *Edge Case:* You can upgrade the same cube twice, e.g., yellow → red → green.
   - **Trade Cards:** Return indicated cubes to bowls and take specified cubes from supply to caravan.
     + *Rule Interaction:* Trade any number of times in a row with available cubes.

2. **Acquire:** Pay for Merchant card by placing ANY cube on each preceding card, then take acquired card into hand.
   - *Strategic Consideration:* Acquire cards that synergize with your current collection or upcoming Point cards.

3. **Rest:** Take all played face-up cards back into hand to build Merchant deck.
   - *Edge Case:* You cannot Rest if you didn't play any cards this turn.

4. **Claim:** Collect indicated cubes from caravan, return them to bowls, take Point card face down, and place gold/silver tokens as needed.
   - *Rule Interaction:* Sliding Point cards fills empty slot and draws new card from deck.

**Endgame:**

- Game ends after fifth Point card is claimed (sixth in 2-3 player games).
- Score points: Point cards + Gold/Silver tokens + Non-yellow cubes on caravan. Gold = 3 points, Silver = 1 point, Other cubes = 1 point each.
- Tiebreaker: Last player to take a turn wins.

**Strategic Considerations:**

- Balance cube acquisition and trading for maximum efficiency.
- Prioritize Point cards that offer more valuable rewards (e.g., gold tokens).
- Monitor opponents' caravans to anticipate their moves and block potential Point cards.
- Build your Merchant deck strategically, acquiring cards that complement each other's effects.

**Expert Tips:**

1. Focus on yellow cubes early for trading flexibility.
2. Prioritize high-value trades over small ones.
3. Keep track of upcoming Point cards and plan accordingly.
4. Pay attention to opponents' Merchant decks; acquired cards can reveal their intentions.
5. Consider claiming multiple Point cards in one turn when possible to deny opponents valuable rewards.

**Edge Cases & Interactions:**

- Trading cubes beyond what's needed for a trade wastes resources, so be mindful of cube limits and supply availability.
- When acquiring a card with cubes on it, those cubes go directly onto your caravan without occupying any spaces.
- If you claim the leftmost or second-leftmost Point card without taking gold/silver tokens, don't slide piles as there are no empty slots to fill.
```

</details>
