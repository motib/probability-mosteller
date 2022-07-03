# Problem 5. Coin in a square

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def find_crossings(side, radius):
    # Count of crossings
    crossings = 0

    for i in range(n):
        # Generate random center coordinates
        x = random.random() * side
        y = random.random() * side

        # Crossing if x/y  +/- side outside the square
        if (x + radius > side) or (x - radius < 0):
            crossings += 1
        elif (y + radius > side) or (y - radius < 0):
            crossings += 1

    print('Probability of landing within the square = {:.4f}'.
          format((side-2*radius)**2 / (side)**2))
    print('Proportion landing within the square     = {:.4f}'.
          format(1.0-(crossings/n)))

def simulate():
    # Tuple is (side of the square, radius of the coin)
    for s in [(8,1), (8,2), (8,3), (8,4)]:
        print('For side = {:1d}, radius = {:1d}:'.
              format(s[0], s[1]))
        find_crossings(s[0], s[1])

simulate()
