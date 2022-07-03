# Problem 37. Bold play vs. cautious play

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# Take a chance that infinite movement will not occur!
def simulate():
    bold_wins     = 0
    cautious_wins = 0

    for j in range(n):
        # Bold play
        if random.randint(1,38) <= 18:
            bold_wins += 1

        # Cautious play
        i = 1
        amount = 20
        # Move until moved to zero or end
        while amount != 0 and amount != 40:
            if random.randint(1,38) <= 18:
                amount += 1
            else:
                amount -= 1
            i += 1
        if amount == 40:
            cautious_wins += 1

    p_bold = 18.0/38.0
    r = 18.0/20.0
    p_cautious = (1-(1/r)**20) / (1-(1/r)**40)

    print('Probability of bold wins     = {:.4f}'.
          format(p_bold))
    print('Proportion bold wins         = {:.4f}'.
          format(bold_wins/n))
    print('Probability of cautious wins = {:.4f}'.
          format(p_cautious))
    print('Proportion cautious wins     = {:.4f}'.
          format(cautious_wins/n))

simulate()
