# Problem 15. The theater row

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def arrange_row(places):
    # Number of odd numbers
    # half+1 is number of even numbers
    half = places // 2
    pairs = 0

    for i in range(n):
        bins = [0] * places
        evens = odds = 0
        
        # Fill places with 0 = even, 1 = odd
        for j in range(half):
            bins[j] = 0
        for j in range(half+1,places):
            bins[j] = 1
        # Randomize the arrangement
        random.shuffle(bins)

        # Check for adjacent even/odd pairs
        for j in range(places-1):
            if bins[j] != bins[j+1]:
                pairs += 1

    print('Expectation of different pairs = {:.4f}'.
          format((places-1) * (half+1) / places))
    print('Average different pairs        = {:.4f}'.\
        format(pairs / n))

def simulate():
    for p in [5, 15, 27, 49]:
        print('For {:2d} places:'.format(p))
        arrange_row(p)

simulate()
