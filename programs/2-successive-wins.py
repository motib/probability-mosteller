# Problem 2. Successive wins

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def play_games(p1, p2):
    # Counts of which scenario wins
    p121_wins = 0
    p212_wins = 0

    for i in range(n):

        # Generate random outcomes that you win
        #   two games against P1 and two games against P2
        # Two games for P1
        g1_1 = random.random()
        g1_2 = random.random()
        # Two games for P2
        g2_1 = random.random()
        g2_2 = random.random()

        # Check which scenario is better
        # p121: you win the first two games
        #       or the second two games (g2_2 not needed)
        if (p1 > g1_1 and p2 > g2_1) or \
           (p2 > g2_1 and p1 > g1_2):
                p121_wins += 1
        # p212: you win the first two games or
        #       or the second two games (g1_2 not needed)
        if (p2 > g2_1 and p1 > g1_1)   or \
           (p1 > g1_1 and p2 > g2_2):
                p212_wins += 1

    print('For p1 = {:.1f}, p2 = {:.1f}'.format(p1, p2))
    print('Proportion of P_121 wins = {:.4f}'.
        format(p121_wins/n))
    print('Proportion of P_212 wins = {:.4f}'.
        format(p212_wins/n))
    print()

def simulate():
    for p in [(.6,.5), (.6,.4), (.6,.2)]:
        play_games(p[0],p[1])

simulate()
