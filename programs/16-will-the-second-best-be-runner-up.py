# Problem 17. Twin knights

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def play_tournament(p):
    successes = 0
    players = 2**p

    for i in range(n):
        played = False

        # Fill bins and shuffle
        bins = [v for v in range(players)]
        random.shuffle(bins)
        # For pairs of players whose games differ by 2
        #   determine a winner for 4 pairs and then 2 pairs, etc.
        for d in range(p-1):
            for j in range(0,players//2**d,2):
                if bins[j] > bins[j+1]:
                    bins[j//2] = bins[j+1]
                else:
                    bins[j//2] = bins[j]

        # Did 0 and 1 play the last game?
        if bins[0] + bins[1] == 1:
            played = True

        # Check for success
        if played:
            successes += 1

    print('Probability a2 is runner-up                = {:.4f}'.
          format((2**(p-1))/((2**p)-1)))
    print('Proportion of games where a2 is runner-up  = {:.4f}'.
          format(successes/n))

def simulate():
    for p in [3,5,7]:
        print('For {:3d} players:'.format(2**p))
        play_tournament(p)

simulate()
