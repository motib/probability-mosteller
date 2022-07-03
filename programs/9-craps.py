# Problem 9. Craps

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def simulate():
    games_won = 0
    for j in range(n):

        # First throw of the dice
        sum  = random.randint(1,6) + random.randint(1,6)

        # Decide if outcome is win, loss or point
        if sum == 2 or sum == 3 or sum == 12:
            continue
        elif sum == 7 or sum == 11:
            games_won += 1
            continue
        else:
            point = sum

        # A point was thrown so continue playing
        # Stop at 7 (lose) or point (win)
        # sum = 0 to prevent immediate termination
        sum = 0
        while sum != 7 and sum != point:
            # Throw two dice
            sum  = random.randint(1,6) + random.randint(1,6)
            if sum == point:
                games_won += 1

    print('Probability of winning = 0.4929')
    print('Proportion of wins     = {:.4f}'.
          format(games_won/n))

simulate()
