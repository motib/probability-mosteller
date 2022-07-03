# Problem 4. Trials Until First Success

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# Simulate throws of the die
def simulate():
    # Bins for counting occurrences of
    #   number of throws
    # If greater than 500 or an error will occur!
    bins = [0] * 500

    for i in range(n):
        die = 0
        throws = 0
        # Throw until 6 received
        while die != 6:
            die = random.randint(1,6)
            throws += 1
        # Increment the bin for number of throws
        bins[throws] += 1

    # Compute weighted average
    average = 0
    for m in range(len(bins)):
        average += m * bins[m]
    print('Expectation of first success = 6')
    print('Average of first success     = {:.4f}'.
          format(average / n))

simulate()
