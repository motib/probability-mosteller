# Problem 47. Choosing the largest dowry

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def guess_largest(cards, select):
    games_won = 0
    for i in range(n):
        won = True

        # Create list of cards and shuffle
        bins = [c for c in range(cards) if True]
        random.shuffle(bins)

        # Arbitrarily take last card as largest
        largest = bins.index(cards-1)
        # Find maximum among 0..select
        max_select = max(bins[:select])

        # Compare to largest
        if max_select == bins[largest]:
            won = False
        else:
            for m in range(select, largest):
                if bins[m] > max_select:
                    won = False

        # Accumulate wins
        if won:
            games_won += 1

    print('Reject cards before r = {:2d}:'.
          format(select))
    print('Probability of wins   = {:.4f}'.
          format(-((select-1)/cards) *
                 math.log((select-1)/cards)))
    print('Proportion wins       = {:.4f}'.
      format(games_won/n))

def simulate():
    cards = 100
    print('Number of cards = {:d}'.format(cards))
    for select in [36, 37, 38, 30]:
        guess_largest(cards, select)

simulate()
