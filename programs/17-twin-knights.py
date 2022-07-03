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
        #   determine a winner for players separated by
        #   players//2, players//4, players//8
        for d in range(p-1):
            for j in range(0,players//2**d,2):
                # If 0, 1 played each other, success
                if bins[j] + bins[j+1] == 1:
                    played = True
                    break
                # Otherwise, assign a random winner
                else:
                    if random.randint(0,1) == 0:
                        bins[j//2] = bins[j+1]
                    else:
                        bins[j//2] = bins[j]

        # Did 0 and 1 play
        if bins[0] + bins[1] == 1:
            played = True

        # Check for success
        if played:
            successes += 1

    print('Probability that a1, a2 meet = {:.4f}'.
          format(1/2**(p-1)))
    print('Proportion a1, a2 meet       = {:.4f}'.
          format(successes/n))

def simulate():
    for p in [3,5,7]:
        print('For {:3d} players:'.format(2**p))
        play_tournament(p)
simulate()
