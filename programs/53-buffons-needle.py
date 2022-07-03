# Problem 53. Buffon's needle

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def probability_of_crossing(length):
    crossings = 0.0

    for i in range(n):
        # Get random center and angle of needle

        center = random.random()
        theta = (math.pi/2.0) * random.random()
        # Compute if projection crosses
        if center <= length*math.sin(theta):
            crossings += 1

    print('Expectation of crossings = {:.4}'.
          format(2.0*length/math.pi))
    avg_crossings = crossings/n
    print('Average crossings        = {:.4}'.
          format(avg_crossings))
    print('Empirical value for pi   = {:.5}\n'.
          format(2.0*length/avg_crossings))

def simulate():
    for length in [0.2,0.5,1.0]:
        print('For length = {:.2}:'.format(length))
        probability_of_crossing(length)

simulate()

