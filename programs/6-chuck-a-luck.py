# Problem 5. Coin in a square

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    total_winnings = 0
    for i in range(n):
        winnings = 0

        # Generate random throws
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)

        # Chosen number is arbitrarily 1
        if d1 == 1: winnings += 1
        if d2 == 1: winnings += 1
        if d3 == 1: winnings += 1

        # Lose $1 if 1 does not appear on any die
        if d1 != 1 and d2 != 1 and d3 != 1:
            winnings -= 1

        # Accumulate total winnings
        total_winnings += winnings

    print('Expectation of winnings = -0.0787')
    print('Average winnings        = {:.4f}'.
          format(total_winnings/n))

simulate()
