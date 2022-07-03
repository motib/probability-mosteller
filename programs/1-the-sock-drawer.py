# Problem 1. The sock drawer

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def draw_socks(red, black):
    both_red = 0

    for i in range(n):
        # Place red and black sock in drawer
        drawer = ['r' for s in range(red)] + \
                 ['b' for s in range(black)]
        # Shuffle to obtain a random arrangement
        random.shuffle(drawer)

        # Draw two socks without replacement
        first_sock  = random.sample(drawer,k=1)
        drawer.remove(first_sock[0])
        second_sock = random.sample(drawer,k=1)
        # Check for two red
        if first_sock[0]  == 'r' and \
           second_sock[0] == 'r':
            both_red += 1

    print('Average of both red for ' +
          '(red = {:2d}, black = {:2d}) = {:.4f}'.
          format(red, black, both_red / n))

def simulate():
    print('Expectation of both red  = 0.5000')
    # Tuples (red, black)
    for socks in [(3,1), (15,6), (85,35)]:
        draw_socks(socks[0], socks[1])

simulate()
