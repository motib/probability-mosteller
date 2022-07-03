# Problem 35. The cliff hanger

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000


def step_until_zero(prob):
    successes = 0
    max_steps = 500  # To stop loop if too many steps

    for j in range(n):
        i = 1
        current_step = 1

        # Move until reached 0 or max_steps
        while     current_step != 0 \
              and i < max_steps:
            if random.random() < prob:
                current_step += 1
            else:
                current_step -= 1
            i += 1

        # Success if reached 0
        if current_step == 0:
            successes += 1

    print('Probability of reaching 0 = {:.4f}'.
          format(min(1,(1-prob)/prob)))
    print('Proportion reaching 0     = {:.4f}'.
          format(successes / n))

def simulate():
    for p in [1/4, 1/2, 2/3, 3/4, 4/5]:
        print('For probability = {:.4f}:'.format(p))
        step_until_zero(p)

simulate()
