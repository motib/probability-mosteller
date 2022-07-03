# Problem 18. An-even-split-at-coin-tossing.py

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def toss_coins(tosses):
    successes = 0

    for i in range(n):
        heads = 0
        # Toss the coins and count heads
        for j in range(tosses):
            if random.randint(1,2) == 1:
                heads += 1

        # Success if head is exactly half of tosses
        if heads == tosses // 2:
            successes += 1

    prob = math.comb(tosses, tosses//2) / 2**tosses
    print('Probability of {:2d} heads for {:3d} tosses = {:.4f}'.
          format(tosses // 2, tosses, prob))
    print('Proportion  of {:2d} heads for {:3d} tosses = {:.4f}'.
          format(tosses // 2, tosses, successes/n))

def simulate():
    for t in [20, 40, 100]:
        toss_coins(t)

simulate()
