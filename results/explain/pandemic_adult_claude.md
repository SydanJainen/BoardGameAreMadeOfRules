---
game: pandemic
audience: adult
model: claude-opus-4
task: explain
---

# Pandemic - Rules Explanation

## Overview

Pandemic is a cooperative board game for 2-4 players, designed by Matt Leacock and published by Z-Man Games. Players form a disease control team tasked with discovering cures for four deadly diseases (represented by blue, yellow, black, and red cubes) that are spreading across the globe. All players win or lose together. A typical session lasts approximately 45 minutes.

## Objective

The sole victory condition is to **discover cures for all four diseases**. Importantly, you do not need to eradicate the diseases or remove all cubes from the board -- simply discovering all four cures at any point during the game triggers an immediate collective victory.

## Components

- 1 game board (world map with 48 cities connected by routes)
- 5 role cards and 5 matching pawns
- 6 research stations
- 96 disease cubes (24 per color: blue, yellow, black, red)
- 59 player cards (48 city cards, 6 epidemic cards, 5 special event cards)
- 48 infection cards
- 6 markers (4 cure markers, 1 outbreak marker, 1 infection rate marker)
- 4 reference cards

## Setup

1. Place the board centrally. Each player receives a random Role card and places their pawn in Atlanta.
2. Place 1 Research Station in Atlanta.
3. Set the Outbreaks Marker to 0 and the Infection Rate Marker to the first position (rate of 2).
4. Deal starting hands based on player count: 4 cards each (2 players), 3 each (3 players), or 2 each (4 players).
5. Remove the 6 Epidemic cards from the Player deck before dealing.
6. **Seed initial infections**: Draw 3 Infection cards and place 3 cubes on each city shown; draw 3 more and place 2 cubes each; draw 3 final cards and place 1 cube each. Discard all 9 cards face-up.
7. **Prepare the Player Draw Pile**: Divide the remaining Player cards into equal piles (4 piles for Introductory, 5 for Normal, 6 for Heroic difficulty). Shuffle one Epidemic card into each pile, then stack the piles to form the draw deck.
8. The most recently ill player goes first.

## Turn Structure

Each turn consists of three sequential phases:

### Phase 1: Take 4 Actions

Choose any combination of the following actions (repeats allowed):

**Movement Actions:**
- **Drive/Ferry** -- Move to an adjacent city (connected by a red line). Routes wrap around the board edges.
- **Direct Flight** -- Discard a city card to move to that city.
- **Charter Flight** -- Discard the card matching your current city to move to any city on the board.
- **Shuttle Flight** -- Move from one Research Station to any other Research Station.

**Special Actions:**
- **Build a Research Station** -- Discard the card matching your current city to place a Research Station there. If all 6 are already placed, you must relocate one.
- **Treat Disease** -- Remove 1 disease cube of any color from your current city. If the disease is already cured, remove all cubes of that color from the city for a single action.
- **Share Knowledge** -- Transfer a city card between two players who are both in the city matching that card. Both players must be co-located, and only the card of the shared city may be exchanged.
- **Discover a Cure** -- At a Research Station, discard 5 cards of one color to cure that disease. Place the corresponding Cure Marker vial-side up.

**Pass** -- A player may pass and forfeit remaining actions.

### Phase 2: Draw 2 Player Cards

Draw 2 cards from the Player Draw Pile. If either card is an **Epidemic**, resolve it immediately (see below). If the draw pile is empty when you need to draw, the game ends in defeat.

**Hand Limit**: Players may hold a maximum of 7 cards. Any excess must be discarded immediately. Special Event cards may be played instead of discarded to stay within the limit.

**Special Event Cards**: These may be played at any time, even during another player's turn, without costing an action.

### Phase 3: Infect Cities

Draw cards from the Infection Draw Pile equal to the current Infection Rate (starts at 2, increases via Epidemics). For each card drawn, place 1 disease cube of the matching color on the indicated city. If the disease color has been eradicated, ignore the card.

## Epidemics

When an Epidemic card is drawn, resolve three steps in order:

1. **Increase** -- Advance the Infection Rate Marker one space on the track.
2. **Infect** -- Draw the **bottom** card of the Infection Draw Pile and place 3 cubes on the indicated city (triggering an outbreak if it would exceed 3). Discard the card.
3. **Intensify** -- Shuffle the entire Infection Discard Pile and place it **on top** of the remaining Infection Draw Pile. This ensures recently infected cities will be drawn again soon.

## Outbreaks

When a city would receive a 4th cube of a single color, an **outbreak** occurs instead:
- Do not place the 4th cube.
- Place 1 cube of the outbreaking color in every adjacent city.
- Advance the Outbreaks Marker by 1.
- **Chain reactions**: If an adjacent city also exceeds 3 cubes, it outbreaks as well. Each city may only outbreak once per chain reaction sequence.

## Eradication

If a disease has been cured and all cubes of that color are subsequently removed from the board, the disease is **eradicated**. Flip the Cure Marker to the sunset side. Eradicated diseases no longer place cubes when their Infection cards are drawn.

## Defeat Conditions

The players lose immediately if any of these occur:
- The Outbreaks Marker reaches 8.
- A player needs to place disease cubes and none remain in the supply of that color.
- A player cannot draw 2 cards from the Player Draw Pile.

## Player Roles

Each role provides a unique ability:

- **Medic** -- Removes all cubes of one color from a city with a single Treat Disease action. Additionally, when a cure is discovered, the Medic automatically removes cubes of that color from any city she enters (or occupies), without spending actions.
- **Scientist** -- Needs only 4 cards (instead of 5) of the same color to Discover a Cure.
- **Researcher** -- May give any card from his hand during Share Knowledge (not just the card matching the current city). Receiving cards still follows the normal restriction.
- **Operations Expert** -- May build a Research Station in his current city without discarding a card.
- **Dispatcher** -- May move other players' pawns using any movement action as if they were his own. May also move any pawn to a city containing another pawn. Requires the other player's consent.

## Information Rules

- In Normal and Heroic games, players may not show their hands but may verbally communicate card holdings.
- In the Introductory game, hands may be played openly.
- Both discard piles (Player and Infection) may be examined freely at any time.

## Difficulty Scaling

The number of Epidemic cards determines difficulty:
- **Introductory**: 4 Epidemics
- **Normal**: 5 Epidemics
- **Heroic**: 6 Epidemics
