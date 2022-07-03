# Problem 44. Winning an unfair game

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

# Take a chance that infinite movement will not occur!
def play_games(prob, games):
    games_won = 0

    for i in range(n):
        wins = 0
        # For each game obtain a random outcome
        for g in range(games):
            if random.random() < prob:
                wins += 1

        # Win if more than half of the games are won
        if wins > games // 2:
            games_won += 1

    print('For {:2d} games, average won   = {:.4f}'.
          format(games, games_won/n))

# Compute optimal number of games for the probability
def optimal_games(prob):
    opt = 1/(1-2*prob)
    low  = math.floor(opt)
    high = math.ceil(opt)

    # If both even, return closer integer
    if low % 2 == 0 and high % 2 == 0:
        if opt - low < high - opt:
            return low
        else:
            return high
    # Otherwise, return the even integer
    elif low % 2 == 0:
        return low
    else:
        return high

def simulate():
    for p in [.33, .37, .4, .45]:
        print('For probability             = {:.4f}'.format(p))
        print('Optimal games to be played  = {:d}'.format(optimal_games(p)))
        for g in [2,4,6,8,10,12,14]:
            play_games(p, g)
        print()

simulate()
