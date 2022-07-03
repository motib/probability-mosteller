# Problem 51. Two-dimensional random walk

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 100

# Max number of steps
# Many steps to increase chance
#   of returning to origin
max_steps = 1000000

def simulate():
    successes = 0
    for j in range(n):
        x, y = 0, 0

        # Take steps +/-x and +/-y
        for s in range(max_steps):
            if random.random() < 0.5:
                x -= 1
            else:
                x += 1
            if random.random() < 0.5:
                y -= 1
            else:
                y += 1

            # Returned to origin
            if x == 0 and y == 0:
                successes += 1
                break

    print('Probability of returning to origin = 1')
    print('Proportion returned to origin      = {:.4f}'.
          format(successes / n))

simulate()
