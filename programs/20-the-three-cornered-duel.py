# Problem 19. Isaac Newton helps Samuel Pepys

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def duel_1():
    wins = 0
    for i in range(n):
        # A misses C
        if random.random() < 0.7:
            # A hits B
            if random.random() < 0.3:
                wins += 1
        # If A hits C, he loses

    print('Expectation of wins = 0.2100')
    print('Average wins        = {:.4f}'.
          format(wins/n))

def duel_2():
    wins = 0
    for i in range(n):
        # A misses B
        if random.random() < 0.7:
            # A has a second chance to hit B
            #   after B hits C
            if random.random() < 0.3:
                wins += 1
        else:
            # A hits B
            # A and C fire at each other
            # Ignore possibility of infinite misses
            while True:
                # C hits A
                if random.random() < 0.5:
                    break
                # C misses A and A hits C
                elif random.random() < 0.3:
                    wins += 1
                    break

    print('Expectation of wins = 0.2792')
    print('Average wins        = {:.4f}'.
          format(wins/n))

def duel_3():
    wins = 0
    for i in range(n):
        # A hits B after firing in the air
        if random.random() < 0.3:
                wins += 1

    print('Expectation of wins = 0.3000')
    print('Average wins        = {:.4f}'.
          format(wins/n))

def simulate():
    print('For A fires first at C:')
    duel_1()
    print('For A fires first at B:')
    duel_2()
    print('For A fires in the air:')
    duel_3()

simulate()
