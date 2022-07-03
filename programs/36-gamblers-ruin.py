# Problem 36. Gambler's ruin

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# Take a chance that infinite movement will not occur!
def step_until_zero_or_n(prob, start_at):
    end_path = 10  # End of path
    reached_zero = 0
    reached_end  = 0

    for j in range(n):
        current_step = start_at

        # Move until reached zero or end
        while current_step != 0 and \
              current_step != end_path:
            if random.random() < prob:
                current_step += 1
            else:
                current_step -= 1

        # Count of reached zero or end
        if   current_step == 0:
            reached_zero += 1
        elif current_step == end_path:
            reached_end += 1

    r = (1.0-prob) / prob
    prob_start = (1-(1/r)**(end_path-start_at)) / \
                 (1-(1/r)**end_path)
    prob_end   = (1-r**start_at) / (1-r**end_path)

    print('Probability of reaching (0,10) from {:d} = ({:.4f},{:.4f})'.
          format(start_at, prob_start, prob_end))
    print('Proportion reaching     (0,10) from {:d} = ({:.4f},{:.4f})'.
          format(start_at, reached_zero/n, reached_end/n))

def simulate():
    for p in [2/3, 3/4, 4/5, 5/6]:
        print('For probability = {:.4f}:'.format(p))
        for m in [1, 4, 6, 8]:
            step_until_zero_or_n(p,m)
        print()

simulate()
