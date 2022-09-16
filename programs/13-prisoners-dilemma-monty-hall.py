# Problem 12. Prisoner's dilemma

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# There is no simulation of the prisoner's dilemma
#   because the probability doesn't change

# This program performs a simulation of
#   the Monty Hall problem

import random

def play_games(games):
    wins_stay   = 0   # Count of games won by staying
    wins_change = 0   # Count of games won by changing

    # doors: False for goat, True for car
    for g in range(games):
        doors = [False, False, False]
        doors[random.randint(0,2)] = True

        # Wlog contestant chooses door 0
        if doors[0]:
            wins_stay += 1
        else:
            wins_change += 1

    print('Games = {:d}'.format(games))
    print('Wins when staying with original door = {:.4f}'.
          format(wins_stay / games))
    print('Wins when changing door              = {:.4f}\n'.
          format(wins_change / games))

def simulate():
    for games in (1000, 10000, 100000):
        play_games(games)

simulate()
