# Problem 25. Lengths of random chords

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

# Simulate using the third method of choosing a random chord
def simulate():
    long_chords = 0

    # The first point is arbtrarily chosen as 0 radians
    # The second is chosen randomly in range 0 to pi
    #   since +/- is symmetric
    for i in range(n):
        point = random.random() * math.pi

        # Long chord if difference > 60 deg = 2*pi/6 rad
        if point > (2.0*math.pi) / 6.0:
            long_chords += 1

    print('Probability of long chords = 0.6667')
    print('Proportion of long chords  = {:.4f}'.
          format(long_chords/n))

simulate()
