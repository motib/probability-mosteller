# Problem 43. The broken bar

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    sum_min = 0.0
    sum_max = 0.0

    for i in range(n):
        # Two random breaks
        left_break  = random.random()
        right_break = random.random()

        # Position of right break must be greater than
        #   position of left break
        if left_break > right_break:
            left_break, right_break = right_break, left_break

        # Accumulate minimum and maximum
        sum_min += min(left_break,
                       right_break-left_break,
                       1-right_break)
        sum_max += max(left_break,
                       right_break-left_break,
                       1-right_break)

    print('Expectations: shortest = {:.4}'.format(2/18) +
          ', middle = {:.4}'.format(5/18) +
          ', longest = {:.4}'.format(11/18))
    print('Averages:     shortest = {:.4}, '.
          format(sum_min/n) +
          'middle = {:.4}, longest = {:.4}'.
          format(1-(sum_min+sum_max)/n, sum_max/n))

simulate()
