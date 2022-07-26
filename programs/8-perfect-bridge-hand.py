# Problem 8. Perfect bridge hand

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

cards  = 16
select = 4

def simulate():
    perfect = 0

    # Construct a random deck with [0,0,0,0,...,3,3,3,3]
    for i in range(n):
        deal = []
        for j in range(cards//select):
            deal = deal + select*[j]
        random.shuffle(deal)

        # Check if the first "select" cards are the same suit
        first = deal[0]
        found = True
        for k in range(1,select):
            if first != deal[k]:
                found = False
                break
        if found:
            perfect += 1

    print('Probability of perfect hand = {:.4f}'.
          format(4.0 / math.comb(cards, select)))
    print('Proportion perfect hand     = {:.4f}'.
           format(perfect / n))

simulate()
