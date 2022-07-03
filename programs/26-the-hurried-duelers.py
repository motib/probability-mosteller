# Problem 26. The hurried duelers

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    meetings = 0
    for i in range(n):
        # Meeting if A and B
        #   randomly choose times within
        #   5 minutes of each other
        # Choose (continuous) times in seconds
        A = random.random() * 3600.0
        B = random.random() * 3600.0

        if abs(A - B) <= 300.0:
            meetings += 1

    print('Probability of meeting   = 0.1597')
    print('Proportion of meetings   = {:.4f}'.
          format(meetings/n))

simulate()
