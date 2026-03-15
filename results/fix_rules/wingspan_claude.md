---
game: wingspan
model: claude-opus-4
task: fix_rules
---

ISSUES IDENTIFIED:
1. Component list contains a typo/artifact: line reads "1 goa" followed by "1 goal board" on the next line, suggesting a duplicated/broken entry. It is unclear whether "1 goa" is a separate component or a scanning error for the goal board.
2. The rulebook text contains a typo: "climage change" appears twice (in the Blue-Gray Gnatcatcher flavor text) instead of "climate change."
3. The Eastern Kingbird card text reads "ONCE BETWEEEN TURNS" with three E's instead of "ONCE BETWEEN TURNS."
4. Food icons are stripped or missing throughout the text. Phrases like "gain 1 [blank] from the supply" or "If any are [blank], gain 1 [blank]" lose critical information about which food type is involved. Players reading this text cannot determine which specific food tokens are referenced.
5. The die face showing two food types is described as "With the die face that shows [blank], gain 1 token of either type (not 2 tokens)" but the actual icons for the two food types are missing, making it impossible to know which combination die face is being referenced.
6. The wild food icon explanation states "If a bird's food requirement includes a wild icon, you can use any of the 5 types of food for it" but the wild icon itself is not visually reproduced or described in a way that a reader of this text version could identify it on a card.
7. The habitat icons for forest, grassland, and wetland are listed by name at the end of the "Play a Bird" section but no visual descriptions are provided to help players match them to the symbols on bird cards.
8. The nest type section lists platform, bowl, cavity, and ground nests with a star/wild nest type, but no visual description is given for how each icon actually looks, making identification on cards difficult from the rulebook text alone.
9. The rules for the birdfeeder refill state two conditions: (a) tray is empty, and (b) all dice show the same face. However, the relationship between these is potentially confusing. The rule says you "may first throw all 5 dice back" when all show the same face, but it is not explicit about whether this is mandatory when the tray is empty (it implies it is automatic when empty but optional when all dice match).
10. The "Play a Bird" section mentions paying an egg cost for columns 2-5 but does not clarify what happens in column 1 explicitly. A reader must infer from "there is no egg cost for the first column" in a parenthetical, which could be overlooked.
11. The 2-food-as-wild exchange rule ("you may spend any 2 food tokens as if they are any 1 food token") is stated only within the Play a Bird section. It is not immediately clear whether this applies only to the food cost of playing birds or also to other food expenditures. The sentence "This exchange cannot be used during other parts of the game" clarifies this, but it is buried in a side note rather than called out prominently.
12. The rules do not specify what happens if the bird deck runs out during setup or during the initial deal of 5 bird cards to each player (though this is extremely unlikely with 170 cards).
13. The solo mode (1 player) is mentioned in the player count (1-5 players) but no solo rules are provided in this rulebook text. Players expecting solo rules from the box would need to look elsewhere.
14. The scoring section on page 5 lists "card tucked under a bird card" as worth 1 point each, but the Bird Powers section does not explicitly restate that tucked cards are worth 1 VP each. A player learning about tucking from the powers section alone might miss this scoring information.
15. The rules do not specify a maximum number of cached food tokens on a single bird card or clarify whether the cache limit is unbounded. The text says "there is no limit on how many food tokens you can have by your mat or on your birds," which covers it implicitly, but a dedicated statement on bird-level cache limits would be clearer.

SUGGESTED FIXES:
1. Remove the "1 goa" line from the component list. The correct entry "1 goal board" already appears on the following line. If "1 goa" was intended to be a separate item (e.g., "1 goal mat"), clarify what it is.
2. Correct "climage change" to "climate change" in the Blue-Gray Gnatcatcher flavor text.
3. Correct "ONCE BETWEEEN TURNS" to "ONCE BETWEEN TURNS" in the Eastern Kingbird card text.
4. Replace all missing food icons with textual descriptors in square brackets. For example: "[invertebrate]", "[seed]", "[fish]", "[fruit]", "[rodent]". Each reference to a food icon should include the food type name so the text is self-contained.
5. Describe the combination die face explicitly: "One die face shows an invertebrate/seed combination. When you select this die, gain 1 token of either type (invertebrate or seed), not 2 tokens."
6. Add a textual description of the wild food icon: "The wild icon is depicted as a circle containing all five food type symbols. If a bird's food requirement includes this wild icon, you may pay with any one of the five food types."
7. Add brief visual descriptions of habitat icons: "Forest is depicted as a tree icon, grassland as a grass/prairie icon, and wetland as a water/wave icon. These appear in the upper left corner of each bird card next to the food cost."
8. Add visual descriptions for each nest type: "Platform nests are shown as a flat horizontal structure; bowl nests appear as a rounded cup shape; cavity nests are depicted as a hole in a tree trunk; ground nests are shown as a shallow depression on the ground. Star/wild nests display a star symbol."
9. Clarify the birdfeeder refill rules by separating the two cases more explicitly: "Mandatory refill: If the birdfeeder tray is completely empty (no dice remain in it), immediately throw all 5 dice back into the birdfeeder. Optional refill: If you are about to gain food and all remaining dice in the tray show the same face (even if only 1 die remains), you may choose to throw all 5 dice back into the birdfeeder before gaining food. Note: the invertebrate/seed combination face counts as its own unique face for this purpose."
10. Make the column 1 egg cost explicit: "Column 1 has no egg cost. To play a bird in column 2 or 3, you must discard 1 egg. To play a bird in column 4 or 5, you must discard 2 eggs."
11. Elevate the 2-for-1 food exchange rule into its own clearly marked subsection or callout box: "IMPORTANT: When playing a bird (and only when playing a bird), you may spend any 2 food tokens as a substitute for any 1 required food token. This exchange is not available when spending food for other purposes such as bonus conversions during the Lay Eggs action."
12. Add a note: "In the extremely unlikely event that the bird card deck is exhausted during setup, shuffle any discarded bird cards to form a new deck."
13. Add a note referencing solo rules: "For solo play (1 player), refer to the separate Automa rules included in the Appendix or as a separate rules sheet."
14. Add a reminder in the Bird Powers section under the tucking/flocking description: "Each card tucked under a bird is worth 1 point at the end of the game."
15. Add an explicit clarification: "There is no limit to the number of food tokens that can be cached on a single bird card."

CORRECTED RULES:

### Components (corrected)
- 1 rulebook
- 1 Appendix
- 1 goal board
- 1 bird tray
- 5 player mats
- 1 birdfeeder dice tower
- 1 scorepad
- 170 bird cards
- 26 bonus cards
- 75 egg miniatures
- 5 custom wooden dice
- 40 wooden action cubes
- 103 food tokens
- 8 goal tiles
- 1 first player token

### Blue-Gray Gnatcatcher (corrected flavor text)
"Gnatcatchers' breeding range is steadily shifting north with climate change."

### Eastern Kingbird (corrected power text)
"ONCE BETWEEN TURNS: When another player plays a [forest] bird, gain 1 [invertebrate] from the supply."

### Managing the Birdfeeder (corrected)
The birdfeeder has a tray to hold the 5 food dice. Dice removed from the birdfeeder when a player gains food remain outside the tray until the birdfeeder is refilled.

**Mandatory refill:** If the birdfeeder tray is completely empty (all dice have been removed), immediately throw all 5 dice back into the birdfeeder.

**Optional refill:** If all dice remaining in the tray show the same face (including if there is only 1 die remaining) and you are about to gain food for any reason, you may choose to first throw all 5 dice back into the birdfeeder before selecting dice. The invertebrate/seed combination face counts as its own unique face for this comparison.

### Food Types (clarified)
The 5 types of food are:
- Invertebrate (depicted as a caterpillar icon)
- Seed (depicted as a wheat/grain icon)
- Fish (depicted as a fish icon)
- Fruit (depicted as a berry/fruit icon)
- Rodent (depicted as a mouse icon)

One die face shows a combined invertebrate/seed symbol. When you select this die, gain 1 token of either invertebrate or seed (not both).

**No food cost:** A crossed-out circle on a bird card means that bird has no food cost.

**Wild food:** If a bird's food requirement includes a wild icon (a circle containing all five food symbols), you may use any one of the five food types to satisfy that requirement.

### Egg Cost for Playing Birds (clarified)
When playing a bird onto your player mat, you must pay an egg cost depending on the column:
- Column 1: No egg cost
- Column 2 or 3: Discard 1 egg from any bird(s) on your mat
- Column 4 or 5: Discard 2 eggs from any bird(s) on your mat

### Food Exchange Rule (clarified)
**When playing a bird only:** You may spend any 2 food tokens as a substitute for any 1 required food token. This exchange cannot be used during other parts of the game (e.g., it cannot be used for the food-to-egg bonus conversion on the Lay Eggs row, nor for food costs triggered by bird powers).

### Tucking and Flocking (clarified)
Some bird powers allow you to tuck cards from your hand or from the deck under that bird. This represents the creation of a flock. Each tucked card is worth 1 point at the end of the game. There is no limit to the number of cards that can be tucked under a single bird.

### Caching Food (clarified)
Some bird powers allow you to cache food tokens on the bird card (the bird is saving the food for later). Cached food tokens cannot be spent as regular food; instead, each cached food token is worth 1 point at the end of the game. There is no limit to the number of food tokens that can be cached on a single bird card. If the supply of food tokens runs out, you may cache discarded cards face-down as a substitute.

### Solo Play
For solo play (1 player), refer to the Automa rules included separately in the Appendix. The solo mode uses an automated opponent deck that simulates a second player's actions.
