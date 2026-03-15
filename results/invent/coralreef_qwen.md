---
model: qwen2.5:latest
temperature: 0.6
timestamp: '2026-02-18T14:37:28.415230Z'
execution_time_seconds: 31.7
prompt_length: 3497
model_alias: qwen
tokens: 1390
additional_params:
  retry_info:
    retry_triggered: true
    retry_count: 1
    retry_reason: 'mechanics: Mechanics list is empty; components: Components list
      is empty'
    final_validation_passed: false
---

# **Reef Builders: Coral Kingdoms**

## Theme
In **Reef Builders: Coral Kingdoms**, players embark on a thrilling journey to restore and thrive in the vibrant and complex coral reef ecosystem. As marine biologists, they must meticulously place habitat tiles, attract diverse species, and balance environmental conditions to create thriving biodiversity hotspots. The game simulates the intricate relationships between different marine life forms and their habitats, making every decision crucial for the health of the reef and the success of their conservation efforts.

## Game Details
- **Mechanics**: 
- **Players**: 2-4
- **Duration**: 60 minutes

## Components


## Rules
### Game Name:
**Reef Builders: Coral Kingdoms**

### Theme:
In **Reef Builders: Coral Kingdoms**, players embark on a thrilling journey to restore and thrive in the vibrant and complex coral reef ecosystem. As marine biologists, they must meticulously place habitat tiles, attract diverse species, and balance environmental conditions to create thriving biodiversity hotspots. The game simulates the intricate relationships between different marine life forms and their habitats, making every decision crucial for the health of the reef and the success of their conservation efforts.

### Mechanics:
1. **Tile Placement**: Players must strategically place habitat tiles on a growing coral reef board, considering the specific conditions required by various species.
2. **Species Attraction**: By placing condition tokens on their tiles, players can attract marine life, increasing their points and creating diverse ecosystems.
3. **Resource Management**: Managing resources like food, energy, and maintenance costs to keep the ecosystem healthy and thriving.

### Components:
- 48 Habitat Tiles (12 each: Coral Reef, Mangrove, Seagrass Bed)
- 36 Species Cards (9 each: Clownfish, Sea Turtle, Octopus, Jellyfish, Crab)
- 20 Condition Tokens (5 each: Warm Water, Cold Water, Food Source, Shelter, Pollutant)
- 1 Game Board (hex grid, 37 tiles)
- 1 Rulebook
- 4 Player Boards
- 60 Resource Cards (15 per type: Food, Energy, Maintenance)
- 12 Watchtower Tokens

### Rules:

#### Turn Structure:
1. **Setup Phase** - Mandatory: At the beginning of each turn, players can place up to two Condition Tokens on any of their tiles.
2. **Action Phase** - Mandatory: Players can perform up to three actions per turn (placement, attraction, or maintenance).
3. **Biodiversity Scoring** - Optional: At the end of each player’s turn, the current biodiversity score is calculated.

#### Action Catalog:

1. **Place Habitat Tile**:
   - When: Any phase.
   - Cost: 2 Food and 1 Energy.
   - Resolution: Place a new tile adjacent to an existing one or on an open space (center).
   - Restrictions: Must be adjacent, no overlapping.

2. **Attract Species**:
   - When: Action Phase.
   - Cost: 1 Condition Token per species.
   - Resolution: Draw the corresponding Species Card and place it on your tile with the matching condition token.
   - Restrictions: Each species can only be attracted once per turn.

3. **Build Watchtower**:
   - When: Any phase.
   - Cost: 2 Wood and 1 Stone.
   - Resolution: Place a Watchtower token on any tile (adjacent to an existing structure).
   - Restrictions: Once per turn, no adjacency required.

4. **Maintain Ecosystem**:
   - When: Action Phase.
   - Cost: 1 Maintenance card.
   - Resolution: Discard the card and remove one Condition Token from your tile.
   - Restrictions: Once per turn, can only be done on a tile with existing conditions.

5. **Trade Resources**:
   - When: Any phase.
   - Cost: None.
   - Resolution: Players can trade resources directly or through a common market (if available).
   - Restrictions: Cannot exceed hand size limit (10 cards).

6. **Draw Resource Cards**:
   - When: Setup Phase, End of Turn.
   - Cost: None.
   - Resolution: Draw 2 cards from the Resource Deck and add to your hand.

#### Player Interaction:

- **Trading Resources**: Players can trade resources directly with each other during any phase.
- **Environmental Events**: Random events can affect all players. These are resolved by drawing an event card, which may require a collective action or resource expenditure.
- **Biodiversity Scoring**: While not direct interaction, players indirectly compete through biodiversity scores, which can influence overall game strategy.

#### Resource Flow:

- **Gained**: Through successful habitat placements and species attraction.
- **Spent**: On maintaining ecosystems, attracting species, and other actions.
- **Lost**: Due to environmental events or poor management.
- **Hand Size**: 10 cards per player. Excess cards are discarded.

#### Special Rules:

- **Species Cards**: Each card has a unique effect on the ecosystem (e.g., food production, pollution).
- **Condition Tokens**: Placing these can attract specific species but also limit tile placement.
- **Watchtowers**: Provide bonuses for maintaining conditions and attracting new species.

#### End Game:

The game ends when all Habitat Tiles are placed or after 10 rounds. Players score points based on the number of different species present in their areas, with higher diversity yielding more points. The player with the highest total biodiversity score wins.

#### Example Round:
**Round 1:**
- **Alice**: Places a Coral Reef tile (adjacent to the center), attracts Clownfish and Jellyfish.
- **Bob**: Places a Seagrass Bed adjacent to Alice’s, builds a Watchtower on his tile.
- **Charlie**: Attracts Sea Turtle with Warm Water condition token.

**Round 2:**
- **Alice**: Maintains her Coral Reef, draws two resource cards.
- **Bob**: Builds another Watchtower, trades Food for Energy with Charlie.
- **Charlie**: Places Mangrove next to Seagrass Bed, attracts Octopus and Crab.

This example demonstrates the game flow and shows how different actions can be taken in a single turn.

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
### Game Name:
**Reef Builders**

### Theme:
Players take on the role of marine biologists dedicated to restoring a thriving coral reef ecosystem. The game simulates the complex interactions between different species and their habitats, requiring players to strategically place tiles, attract marine life, and balance the ecosystem's health. The narrative revolves around the challenges faced by marine conservation efforts in the face of environmental degradation, making every decision count towards preserving biodiversity.

### Mechanics:
1. **Tile Placement**: Players must carefully select where to place habitat tiles on a growing coral reef, considering the species that can thrive there.
2. **Species Attraction**: By placing specific conditions (e.g., temperature, food sources), players can attract marine life, increasing their points and creating biodiversity patterns.
3. **Resource Management**: Managing resources like food, energy, and maintenance costs to keep the ecosystem healthy.
4. **Biodiversity Scoring**: Points are awarded based on the variety of species present in a player’s area, encouraging balanced ecosystems.
5. **Environmental Challenges**: Random events can disrupt the reef, requiring players to adapt their strategies.

### Components:
- 48 Habitat Tiles (12 each: Coral Reef, Mangrove, Seagrass Bed)
- 36 Species Cards (9 each: Fish, Sea Turtle, Crab, Jellyfish, Octopus)
- 20 Condition Tokens (5 each: Warm Water, Cold Water, Food Source, Shelter, Pollutant)
- 1 Game Board (hex grid, 37 tiles)
- 1 Rulebook
- 4 Player Boards
- 60 Resource Cards (15 per type: Food, Energy, Maintenance)
- 12 Watchtower Tokens
- 2 Timer Dice

### Players:
1-4 players

### Duration:
40-60 minutes

### Setup:

1. **Board Assembly**: Place the game board flat on a table.
2. **Deck Preparation**:
   - Shuffle the Habitat Tiles and place them in a draw pile near the board.
   - Shuffle the Species Cards and Condition Tokens separately, then place them face down in designated areas (Resource Deck, Condition Deck).
3. **Initial Resource Distribution**: Each player draws 5 Food cards, 4 Energy cards, and 3 Maintenance cards from the Resource Deck. Place these on their Player Board.
4. **Starting Positions**: Players choose starting tiles from the Habitat Tiles pile and place them adjacent to each other in a hexagonal pattern (the center tile is usually left open for flexibility).
5. **First Player Selection**: Use the two Timer Dice to determine the first player. The player who rolls higher goes first, with ties resolved by rolling again.

### Rules:

#### A) Turn Structure:
1. **Setup Phase** - Mandatory: Each turn starts with players checking and placing any available Condition Tokens on their tiles.
2. **Action Phase** - Mandatory: Players can perform up to three actions per turn (placement, attraction, or maintenance).
3. **Biodiversity Scoring** - Optional: At the end of each player’s turn, the current biodiversity score is calculated.

#### B) Action Catalog:

1. **Place Habitat Tile**:
   - When: Any phase.
   - Cost: 2 Food and 1 Energy.
   - Resolution: Place a new tile adjacent to an existing one or on an open space (center).
   - Restrictions: Must be adjacent, no overlapping.

2. **Attract Species**:
   - When: Action Phase.
   - Cost: 1 Condition Token per species.
   - Resolution: Draw the corresponding Species Card and place it on your tile with the matching condition token.
   - Restrictions: Each species can only be attracted once per turn.

3. **Build Watchtower**:
   - When: Any phase.
   - Cost: 2 Wood and 1 Stone.
   - Resolution: Place a Watchtower token on any tile (adjacent to an existing structure).
   - Restrictions: Once per turn, no adjacency required.

4. **Maintain Ecosystem**:
   - When: Action Phase.
   - Cost: 1 Maintenance card.
   - Resolution: Discard the card and remove one Condition Token from your tile.
   - Restrictions: Once per turn, can only be done on a tile with existing conditions.

5. **Trade Resources**:
   - When: Any phase.
   - Cost: None.
   - Resolution: Players can trade resources directly or through a common market (if available).
   - Restrictions: Cannot exceed hand size limit (10 cards).

6. **Draw Resource Cards**:
   - When: Setup Phase, End of Turn.
   - Cost: None.
   - Resolution: Draw 2 cards from the Resource Deck and add to your hand.

#### C) Player Interaction:

- **Trading Resources**: Players can trade resources directly with each other during any phase.
- **Environmental Events**: Random events can affect all players. These are resolved by drawing an event card, which may require a collective action or resource expenditure.
- **Biodiversity Scoring**: While not direct interaction, players indirectly compete through biodiversity scores, which can influence overall game strategy.

#### D) Resource Flow:

- **Gained**: Through successful habitat placements and species attraction.
- **Spent**: On maintaining ecosystems, attracting species, and other actions.
- **Lost**: Due to environmental events or poor management.
- **Hand Size**: 10 cards per player. Excess cards are discarded.

#### E) Special Rules:

- **Species Cards**: Each card has a unique effect on the ecosystem (e.g., food production, pollution).
- **Condition Tokens**: Placing these can attract specific species but also limit tile placement.
- **Watchtowers**: Provide bonuses for maintaining conditions and attracting new species.

#### F) End Game:

The game ends when all Habitat Tiles are placed or after 10 rounds. Players score points based on the number of different species present in their areas, with higher diversity yielding more points. The player with the highest total biodiversity score wins.

#### G) Example Round:
**Round 1:**
- **Alice**: Places a Coral Reef tile (adjacent to the center), attracts Fish and Jellyfish.
- **Bob**: Places a Seagrass Bed adjacent to Alice’s, builds a Watchtower on his tile.
- **Charlie**: Attracts Sea Turtle with Warm Water condition token.

**Round 2:**
- **Alice**: Maintains her Coral Reef, draws two resource cards.
- **Bob**: Builds another Watchtower, trades Food for Energy with Charlie.
- **Charlie**: Places Mangrove next to Seagrass Bed, attracts Octopus and Crab.

This example demonstrates the game flow and shows how different actions can be taken in a single turn.
```

</details>
