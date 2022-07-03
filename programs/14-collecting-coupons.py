# Problem 14. Collecting coupons

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def collect_coupons(coupons):
    draws = 0
    for i in range(n):
        # Bins for counting which numbers have appeared
        bins = [False] * coupons
        finished = False

        # Draw until all numbers appear
        found = False
        while not found:
            # Draw and update bins
            bins[random.randint(0,coupons-1)] = True
            draws += 1
            # Check if all bins True
            found = True
            for c in range(coupons):
                if not bins[c]:
                    found = False

    print('Expectation of draws = {:.4f}'.
          format(coupons * (math.log(coupons) +
                            1.0/coupons + 0.5772)))
    print('Average draws        = {:.4f}'.
          format(draws/n))

def simulate():
    for c in [5, 10, 20]:
        print('For {:2d} coupons:'.format(c))
        collect_coupons(c)

simulate()
