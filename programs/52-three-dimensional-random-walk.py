# Problem 52. Three-dimensional random walk

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 1000

# Max number of steps
max_steps = 1000

def expectation():
    p = 0.0
    for n in range(1,501):
        p += (math.comb(2*n,n)*(1/2)**(2*n) )**3
    return p

def simulate_one_return():
    successes = 0

    for j in range(n):
        x, y, z = 0, 0, 0
        # Take one step in each of x, y, z
        for s in range(max_steps):
            found = False
            if random.random() < 0.5:
                x -= 1
            else:
                x += 1
            if random.random() < 0.5:
                y -= 1
            else:
                y += 1
            if random.random() < 0.5:
                z -= 1
            else:
                z += 1

            # Check if returned to origin
            if x == 0 and y == 0 and z == 0:
                successes += 1
                found = True
                break  
        if found:
            continue

    print('Probability of reaching origin = {:.4f}'.
          format(1.0-
                 (1.0/(expectation()+1))
                 )
          )
    print('Proportion reached origin      = {:.4f}'.
          format(successes / n))

def simulate_total_returns():
    successes = 0

    for j in range(n):
        x, y, z = 0, 0, 0
        # Take one step in each of x, y, z
        for s in range(max_steps):
            if random.random() < 0.5:
                x -= 1
            else:
                x += 1
            if random.random() < 0.5:
                y -= 1
            else:
                y += 1
            if random.random() < 0.5:
                z -= 1
            else:
                z += 1

            # Check if returned to origin
            if x == 0 and y == 0 and z == 0:
                successes += 1

    print('Expectation of reaching origin = {:.4f}'.
          format(expectation()))
    print('Average times reached origin   = {:.4f}'.
          format(successes / n))

simulate_total_returns()
simulate_one_return()
