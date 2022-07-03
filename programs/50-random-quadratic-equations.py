# Problem 50. Random quadratic equations

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def equation(B):
    real_roots = 0
    for i in range(n):
        b = random.uniform(-B, B)
        c = random.uniform(-B, B)
        if b*b - c >= 0:
            real_roots += 1

    print('For B = {:2d}:'.format(B))
    print('Probability of real roots = {:.4f}'.
          format(1.0-(1.0/(3.0*math.sqrt(B)))))
    print('Proportion real roots     = {:.4f}'.
          format(real_roots / n))

def simulate():
    for B in [4, 16, 64]:
        equation(B)

simulate()
