# Problem 45. Average number of matches

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# The expectation is the number of cards before the first ace
def simulate():
    matches = 0

    for i in range(n):
        # Get two decks and shuffle the second deck
        cards1 = [v for v in range(52) if True]
        cards2 = cards1.copy()
        random.shuffle(cards2)

        # Accumulate the matches between the two decks
        for j in range(52):
            if cards1[j] == cards2[j]:
                matches += 1

    print('Expectation of matches = 1.00')
    print('Average matches        = {:2.2f}'.
          format(matches / n))

simulate()
