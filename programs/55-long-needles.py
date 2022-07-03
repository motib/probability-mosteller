# Problem 55. Long needles

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def expectation_long_needles(length):
    return 1.0 + (2.0/math.pi) * \
        (
        length *
            (
            1.0 - math.sqrt(1.0-(1.0/(length*length)))
            ) -
        math.asin(1.0/length)
        )


def probability_of_crossing(length):
    crossings = 0.0

    for i in range(n):
        # Get random center and angle of needle
        center = random.random()
        theta = (math.pi/2.0) * random.random()
        # Compute if projection crosses
        if center <= length*math.sin(theta):
            crossings += 1

    print('Expectation of crossings = {:.4f}'.
          format(expectation_long_needles(length)))
    print('Average crossings        = {:.4f}'.
          format(crossings/n))
    print()

def simulate():
    for length in [1.5,2.0,2.5,3.0]:
        print('For length = {:.1f}:'.format(length))
        probability_of_crossing(length)

simulate()
