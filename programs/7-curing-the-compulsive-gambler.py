# Problem 7. Curing the compulsive gambler

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 1000000

# A game is won if no money lost
def simulate():
    winnings = 0
    for j in range(n):
        if random.random() < 1.0/38.0:
            winnings += 35
        else:
            winnings += -1

    print('Expectation of winning a round = -0.0526')
    print('Average winnings for a round   = {:.4f}'.
          format(winnings/n))

simulate()
