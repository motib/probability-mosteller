# Problem 3. The flippant juror

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# Compute fraction of correct decisions for p
def one_decision(p):
    correct_a = 0
    correct_b = 0

    for i in range(n):
        # Generate random decisions
        # Third juror always has probabiliy 0.5
        juror1 = random.randint(0,1) < p
        juror2 = random.randint(0,1) < p
        juror3 = random.randint(0,1) < 0.5

        # Decision by majority for (a)
        correct_a += (juror1 and juror2) or \
                     (juror1 and juror3) or \
                     (juror2 and juror3)
        # Decision by one juror for (b)
        correct_b += random.randint(0,1) < p

    # At the end of the simulation display the result
    print('For p = {:.2f}, '.format(p) +
          'proportion correct of (a) = {:.4f}, (b) = {:.4f}'.
          format(correct_a/n, correct_b/n))

def simulate():
    print('Prediction: probabilities of (a) and (b) are equal')
    # Run simulation for three probabilities
    for p in [0.25, 0.5, 0.75]:
        one_decision(p)

simulate()
