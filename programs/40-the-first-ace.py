# Problem 50. The first ace

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    steps_to_ace = 0

    for i in range(n):
        # Create random list of 52 cards
        cards = [v for v in range(13) if True] * 4
        random.shuffle(cards)

        # Search for first 0 card
        steps_to_ace += cards.index(0)

    print('Expectation of first ace = {:.4f}'.format(48/5))
    print('Average first ace        = {:.4f}'.
          format(steps_to_ace / n))

simulate()
