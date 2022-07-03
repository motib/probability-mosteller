# Problem 23. Ties in matching pennies

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def probability(coins):
    # With an odd number of coins,
    #   a tie cannot first occur when counting
    #   the last coin
    if coins % 2 == 0:
        return 1.0 - \
               math.comb(coins-1, coins//2) / \
               (2**(coins-1))
    else:
        return probability(coins-1)

def count_coins(coins):
    successes = 0
    for i in range(n):
        # Running counts of odds and evens
        evens = 0
        odds  = 0
        for c in range(coins):
            # Even if two random values are equal
            if random.randint(0,1) == random.randint(0,1):
                evens += 1
            else:
                odds  += 1

            # Success if evens equal odds
            if evens == odds:
                successes += 1
                break

    print('For {:2d} tosses:'.format(coins))
    print('Probability of ties = {:.4f}'.\
            format(probability(coins)))
    print('Proportion of ties  = {:.4f}'.\
           format(successes / n))

def simulate():
    for c in [4, 6, 7, 10, 20]:
        count_coins(c)

simulate()
