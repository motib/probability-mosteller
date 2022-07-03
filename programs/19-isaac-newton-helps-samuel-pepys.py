# Problem 19. Isaac Newton helps Samuel Pepys

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

# Compute expectation from formula
def expectation(d):
    ex = 0
    for m in range(d):
        ex += math.comb(6*d, m) * (1.0/6.0)**m * (5.0/6.0)**(6*d-m)
    return 1.0 - ex

def throw_dice(dice):
    successes = 0

    for i in range(n):
        sixes = 0
        # Throw all dice and count sixes
        for j in range(6*dice):
            if random.randint(1,6) == 6:
                sixes += 1

        # Successes if sixes >= prediction
        if sixes >= dice:
            successes += 1

    print('For {:3d} dice to throw {:2d} sixes:'.
          format(6*dice, dice))
    print('Probability = {:.4f}'.
          format(expectation(dice)))
    print('Proportion  = {:.4f}'.
          format(successes/n))

def simulate():
    # Simulate for various numbers of dice
    for k in [1, 2, 3, 16, 60]:
        throw_dice(k)

simulate()
