# Problem 45. Average number of matches

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def find_exact_matches(r):
    exact_matches = 0
    for i in range(n):
        matches = 0
        # Generate two decks and shuffle the second
        cards1 = [v for v in range(52) if True]
        cards2 = cards1.copy()
        random.shuffle(cards2)

        # For each card compare the two decks
        for j in range(52):
            if cards1[j] == cards2[j]:
                matches += 1

        # Accumulate number of exact matches
        if matches == r:
            exact_matches += 1

    # Estimate for large n-r
    print('Probability of {:1d} matches = {:.4f}'.
          format(r, 1.0/(math.factorial(r)*math.e)))
    print('Proportion {:1d} matches     = {:.4f}'.
          format(r, exact_matches/n))

def simulate():
    for r in range(7):
        find_exact_matches(r)

simulate()
