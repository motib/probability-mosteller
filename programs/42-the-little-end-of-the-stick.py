# Problem 42. The little end of the stick

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def simulate():
    smaller_sum = 0.0
    ratio_sum = 0.0

    for i in range(n):
        # Break the stick at a random point
        the_break  = random.random()
        # Ignore break at left end
        if the_break == 0.0:
            continue
        # Left half is smaller
        if the_break < 0.5:
            smaller = the_break
            larger  = 1 - the_break
        # Right half is smaller
        else:
            smaller = 1 - the_break
            larger  = the_break

        # Accumulate smaller and ratio
        smaller_sum += smaller
        ratio_sum   += smaller / larger

    print('Expectation of length of smaller = {:.4f}'.format(1/4))
    print('Average length of smaller        = {:.4f}'.
          format(smaller_sum / n))
    print('Expectation of smaller/larger    = {:.4f}'.
          format(2*math.log(2)-1))
    print('Average smaller/larger           = {:.4f}'.
          format(ratio_sum / n))

simulate()
