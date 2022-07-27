# Problem 54. Buffon's needle with horizontal and vertical rulings

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
        # Compute if projection crosses horizontal or vertical
        if center <= length*math.sin(theta):
            crossings += 1
        if center <= length*math.cos(theta):
            crossings += 1

    print('Expectation of crossings = {:.4f}'.
          format(4.0*length/math.pi))
    avg_crossings = crossings/n
    print('Average crossings        = {:.4f}'.
          format(avg_crossings))

def simulate():
    for length in [0.2,0.5,1.0]:
        print('For length = {:.2}:'.format(length))
        probability_of_crossing(length)

simulate()

