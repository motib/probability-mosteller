# Problem 39. The clumsy chemist

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    sum = 0.0

    for i in range(n):
        left_break  = random.random()
        right_break = random.random()

        # Make sure that the Position of the right break
        #   is greater than the  position of the left break
        if left_break > right_break:
            left_break, right_break = right_break, left_break
        # Right piece is from right break to end of rod
        sum += (1.0 - right_break)
        
    print('Expectation of length of right piece = 0.3333')
    print('Average length of right piece        = {:.4f}'.
           format(sum / n))

simulate()
