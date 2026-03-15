---
model: qwen2.5:latest
temperature: 0.6
timestamp: '2026-02-18T14:39:15.577866Z'
execution_time_seconds: 39.77
prompt_length: 3488
model_alias: qwen
tokens: 1789
additional_params:
  retry_info:
    retry_triggered: true
    retry_count: 1
    retry_reason: 'mechanics: Mechanics list is empty; components: Components list
      is empty'
    final_validation_passed: false
---

# **Galactic Vortex**

## Theme
In **Galactic Vortex**, players take on the roles of interstellar entrepreneurs navigating a vast and ever-expanding galaxy. The game is set against the backdrop of a universe where resources are scarce and space stations are scattered across uncharted territories. Players must strategically deploy shuttle fleets to connect these stations, forming lucrative trade networks while outmaneuvering competitors. The unpredictable nature of asteroid fields adds an element of chaos, creating dynamic routes that players can exploit or avoid.

## Game Details
- **Mechanics**: 
- **Players**: 2-4
- **Duration**: 60 minutes

## Components


## Rules
### Game Name:
**Galactic Vortex**

### Theme:
In **Galactic Vortex**, players take on the roles of interstellar entrepreneurs navigating a vast and ever-expanding galaxy. The game is set against the backdrop of a universe where resources are scarce and space stations are scattered across uncharted territories. Players must strategically deploy shuttle fleets to connect these stations, forming lucrative trade networks while outmaneuvering competitors. The unpredictable nature of asteroid fields adds an element of chaos, creating dynamic routes that players can exploit or avoid.

### Mechanics:
1. **Route-Building**: Players connect space stations using shuttle fleets, expanding their network across the galaxy map.
2. **Resource Management**: Managing fuel resources is crucial for deploying shuttles; mismanagement leads to stranded assets and penalties.
3. **Asteroid Fields**: Randomly placed asteroid fields can disrupt routes and create strategic opportunities.

#### Explanation of Mechanics:
1. **Route-Building**:
   - Players use shuttle tokens to connect space stations on the hex grid board, forming trade routes.
   - Each successful connection grants a fuel token as compensation.
2. **Resource Management**:
   - Players start with 15 fuel tokens and can gain additional fuel by deploying shuttles or completing mission cards.
   - Mismanagement of fuel results in penalties such as stranded shuttles or reduced operational efficiency.
3. **Asteroid Fields**:
   - Asteroid fields are randomly placed on the board, disrupting routes and creating strategic chokepoints.
   - Players must navigate around these obstacles while still connecting stations.

### Components:
1. **Game Board (hex grid, 40 tiles)**
2. **64 Resource Cards (16 per type: Fuel, Iron Ore, Crystal, Wood, Electronics)**
3. **25 Shuttle Tokens (5 per player color)**
4. **40 Space Station Tiles (8 per player color)**
5. **30 Mission Cards (6 per player color)**
6. **Asteroid Field Markers (16 total)**
7. **Fuel Track (for each player, 20 spaces)**
8. **Player Tokens (5 colors, 1 of each for the board center)**
9. **Rulebook and Setup Guide**

### Rules:
#### Turn Structure:
Each turn consists of the following phases, in order: Resource Phase, Planning Phase, Action Phase, and Cleanup Phase. Each phase is mandatory.

1. **Resource Phase (mandatory)**:
   - Draw 2 Resource Cards from the deck.
   - Discard any number of cards to replenish your hand to a maximum of 5 cards.
2. **Planning Phase (mandatory)**:
   - Decide on actions for the turn, including deploying shuttles and setting up trade negotiations.
3. **Action Phase (mandatory)**:
   - Perform all planned actions in order.
4. **Cleanup Phase (mandatory)**:
   - Resolve any final effects from completed actions.

#### Action Catalog:

1. **Deploy Shuttle**:
   - When: Planning Phase
   - Cost: 2 Fuel tokens per shuttle
   - Resolution: Place a shuttle token on an adjacent space station tile. Gain 1 Fuel token for each shuttle.
   - Restrictions: Cannot deploy shuttles to the same space station as another player.

2. **Build Space Station**:
   - When: Planning Phase
   - Cost: 3 Fuel tokens and 2 Resource Cards (of any type)
   - Resolution: Place a space station tile adjacent to an existing station, gaining its resource.
   - Restrictions: Cannot build on asteroid fields or within 1 hex of another player’s space station.

3. **Trade Negotiation**:
   - When: Planning Phase
   - Cost: 2 Fuel tokens and 1 Resource Card (of any type)
   - Resolution: Engage in a trade with an adjacent player, exchanging resources according to mutual agreement.
   - Restrictions: Cannot negotiate with more than one player per turn.

4. **Discard for Income**:
   - When: Any phase
   - Cost: Discard 2 cards from your hand (any type)
   - Resolution: Gain 1 Fuel token for each card discarded.
   - Restrictions: No limit on frequency, but cannot discard all resources in one turn.

5. **Complete Mission Card**:
   - When: Action Phase
   - Cost: Varies by card; see mission cards for details
   - Resolution: Complete the required route and gain 3 Fuel tokens and any additional specified rewards.
   - Restrictions: Once per turn, can only complete one mission card.

#### Player Interaction:

- **Trading Rules**: Players can trade resources with each other during the Planning Phase. The agreement must be mutual; both players must agree on the exchange of cards before proceeding.
- **Asteroid Fields**: Place 16 asteroid field markers on the board randomly. An asteroid field disrupts routes, preventing shuttles and space stations from being placed there or adjacent to it.

#### Example Round:

**Scenario**: 3 players, Alice, Bob, and Carol, on a game board with asteroid fields.

**Round 1 - Player A: Alice**
1. **Resource Phase**: Draws 2 cards; discards 1 card.
2. **Planning Phase**: Plans to build a space station and deploy a shuttle.
3. **Action Phase**:
   - **Build Space Station**: Places a station adjacent to her existing station, gaining Wood resources.
   - **Deploy Shuttle**: Deploys a shuttle from her initial station to the new station, gaining 1 Fuel token for each shuttle.
4. **Cleanup Phase**: None.

**Round 2 - Player B: Bob**
1. **Resource Phase**: Draws 2 cards; discards none.
2. **Planning Phase**: Plans to trade with Alice and deploy a shuttle.
3. **Action Phase**:
   - **Trade Negotiation**: Agrees to trade Wood for Crystal with Alice, gaining resources.
   - **Deploy Shuttle**: Deploys a shuttle from his initial station to an adjacent station, gaining 1 Fuel token for each shuttle.
4. **Cleanup Phase**: None.

**Round 3 - Player C: Carol**
1. **Resource Phase**: Draws 2 cards; discards none.
2. **Planning Phase**: Plans to deploy shuttles and complete a mission card.
3. **Action Phase**:
   - **Deploy Shuttle**: Deploys shuttles from her stations, gaining Fuel tokens.
   - **Complete Mission Card**: Completes a mission card for 3 additional Fuel tokens and other rewards.
4. **Cleanup Phase**: None.

This example demonstrates the game flow and various actions that players can take in each turn.

### End Game:
The game ends when one player completes all 6 of their color-coded Mission Cards, or after 8 turns if no single player has completed all missions.

**Scoring**:
- Each mission card completion grants 3 Fuel tokens.
- Additional points are awarded for the most space stations built (2 points per station) and the longest continuous route (1 point per hex).

This completes the detailed design of **Galactic Vortex**, ensuring a rich, dynamic, and strategic experience for players.

## Raw LLM Response
<details>
<summary>Click to expand raw response</summary>

```
### Game Name:
**Galactic Vortex**

### Theme:
In **Galactic Vortex**, players take on the roles of interstellar entrepreneurs, seeking to build lucrative trade networks across a chaotic and ever-expanding galaxy. The conflict stems from the scarcity of resources and the unpredictable movements of asteroid fields that threaten these routes. Players must strategically deploy their shuttle fleets to establish profitable connections between space stations while outmaneuvering competitors. The compelling setting is driven by the dynamic nature of space exploration, where fortunes can be made or lost in a single turn due to shifting alliances and unexpected obstacles.

### Mechanics:
1. **Route-Building**: Players connect space stations using shuttle fleets, expanding their network across the galaxy map.
2. **Resource Management**: Managing fuel resources is crucial for deploying shuttles; mismanagement leads to stranded assets.
3. **Asteroid Fields**: Randomly placed asteroid fields can disrupt routes and create strategic opportunities.
4. **Mission Cards**: Secret mission cards provide additional rewards for completing specific routes, adding an element of unpredictability.
5. **Trade Negotiations**: Players can trade resources with each other, forming temporary alliances or competing over shared space.

### Components:
1. **Game Board (hex grid, 37 tiles)**
2. **48 Resource Cards (12 per type: Fuel, Iron Ore, Crystal, Wood)**
3. **20 Shuttle Tokens (5 per player color)**
4. **40 Space Station Tiles (10 per player color)**
5. **60 Mission Cards (10 per player color)**
6. **Asteroid Field Markers (12 total)**
7. **Fuel Track (for each player)**
8. **Player Tokens (5 colors, 1 of each for the board center)**
9. **Rulebook and Setup Guide**

### Players:
2-5 players

### Duration:
45-75 minutes

### SETUP:

1. **Board Assembly**: Place the game board in the middle of the play area.
2. **Deck Preparation**:
   - Shuffle all 48 Resource Cards into a single deck.
   - Shuffle the 60 Mission Cards and place them face-down in a draw pile near the board.
3. **Initial Resource Distribution**:
   - Each player receives 15 Fuel tokens to start the game.
4. **Starting Positions**: 
   - Place each player token on the starting space station tile (randomly chosen by players).
   - The player with the highest roll of a single six-sided die becomes the first player; subsequent turns pass clockwise.
5. **First Player Selection**:
   - The first player is determined as described above.

### RULES:

#### A) TURN STRUCTURE:
Each turn consists of the following phases, in order: Resource Phase, Planning Phase, Action Phase, and Cleanup Phase. Each phase is mandatory.

1. **Resource Phase (mandatory)**:
   - Draw 2 Resource Cards from the deck.
   - Discard any number of cards to replenish your hand to a maximum of 5 cards.
2. **Planning Phase (mandatory)**:
   - Decide on actions for the turn, including deploying shuttles and setting up trade negotiations.
3. **Action Phase (mandatory)**:
   - Perform all planned actions in order.
4. **Cleanup Phase (mandatory)**:
   - Resolve any final effects from completed actions.

#### B) ACTION CATALOG:

1. **Deploy Shuttle**:
   - When: Planning Phase
   - Cost: 2 Fuel tokens per shuttle
   - Resolution: Place a shuttle token on an adjacent space station tile. Gain 1 Fuel token for each shuttle.
   - Restrictions: Cannot deploy shuttles to the same space station as another player.

2. **Build Space Station**:
   - When: Planning Phase
   - Cost: 3 Fuel tokens and 2 Resource Cards (of any type)
   - Resolution: Place a space station tile adjacent to an existing station, gaining its resource.
   - Restrictions: Cannot build on asteroid fields or within 1 hex of another player’s space station.

3. **Trade Negotiation**:
   - When: Planning Phase
   - Cost: 2 Fuel tokens and 1 Resource Card (of any type)
   - Resolution: Engage in a trade with an adjacent player, exchanging resources according to mutual agreement.
   - Restrictions: Cannot negotiate with more than one player per turn.

4. **Discard for Income**:
   - When: Any phase
   - Cost: Discard 2 cards from your hand (any type)
   - Resolution: Gain 1 Fuel token for each card discarded.
   - Restrictions: No limit on frequency, but cannot discard all resources in one turn.

5. **Complete Mission Card**:
   - When: Action Phase
   - Cost: Varies by card; see mission cards for details
   - Resolution: Complete the required route and gain 3 Fuel tokens and any additional specified rewards.
   - Restrictions: Once per turn, can only complete one mission card.

#### C) PLAYER INTERACTION:
- **Trading Rules**: Players can trade resources with each other during the Planning Phase. The agreement must be mutual; both players must agree on the exchange of cards before proceeding.
- **Combat/Conflict Resolution**: No direct combat or conflict resolution in this game. Instead, indirect competition occurs through resource scarcity and strategic placement of space stations.

#### D) RESOURCE FLOW:
- Players start with 15 Fuel tokens and can gain additional fuel by deploying shuttles, completing missions, and discarding cards.
- Resources are gained from trade negotiations but cannot exceed a hand size of 5 cards at any time.
- Resources refresh every turn during the Resource Phase.

#### E) SPECIAL RULES:
- **Asteroid Fields**: Place 12 asteroid field markers on the board randomly. An asteroid field disrupts routes, preventing shuttles and space stations from being placed there or adjacent to it.
- **Mission Cards**: Each mission card has a unique reward for completing specific routes. These are revealed at the start of the game.

#### F) END GAME:
The game ends when one player completes all 10 of their color-coded Mission Cards, or after 6 turns if no single player has completed all missions.

**Scoring**:
- Each mission card completion grants 3 Fuel tokens.
- Additional points are awarded for the most space stations built (2 points per station) and the longest continuous route (1 point per hex).

#### G) EXAMPLE ROUND:

**Scenario**: 2 players, Alice and Bob, on a game board with asteroid fields.

**Round 1 - Player A: Alice**
1. **Resource Phase**: Draws 2 cards; discards 1 card.
2. **Planning Phase**: Plans to build a space station and deploy a shuttle.
3. **Action Phase**:
   - **Build Space Station**: Places a station adjacent to her existing station, gaining Wood resources.
   - **Deploy Shuttle**: Deploys a shuttle from her initial station to the new station, gaining 1 Fuel token for each shuttle.
4. **Cleanup Phase**: None.

**Round 2 - Player B: Bob**
1. **Resource Phase**: Draws 2 cards; discards none.
2. **Planning Phase**: Plans to trade with Alice and deploy a shuttle.
3. **Action Phase**:
   - **Trade Negotiation**: Agrees to trade Wood for Crystal with Alice, gaining resources.
   - **Deploy Shuttle**: Deploys a shuttle from his initial station to an adjacent station, gaining 1 Fuel token for each shuttle.
4. **Cleanup Phase**: None.

**Round 3 - Player A: Alice**
1. **Resource Phase**: Draws 2 cards; discards none.
2. **Planning Phase**: Plans to deploy shuttles and complete a mission card.
3. **Action Phase**:
   - **Deploy Shuttle**: Deploys shuttles from her stations, gaining Fuel tokens.
   - **Complete Mission Card**: Completes a mission card for 3 additional Fuel tokens and other rewards.
4. **Cleanup Phase**: None.

**Round 4 - Player B: Bob**
1. **Resource Phase**: Draws 2 cards; discards none.
2. **Planning Phase**: Plans to deploy shuttles and trade with Alice.
3. **Action Phase**:
   - **Deploy Shuttle**: Deploys a shuttle from his initial station, gaining Fuel tokens.
   - **Trade Negotiation**: Agrees to trade resources with Alice for mutual benefit.
4. **Cleanup Phase**: None.

This example demonstrates the game flow and various actions that players can take in each turn.
```

</details>
