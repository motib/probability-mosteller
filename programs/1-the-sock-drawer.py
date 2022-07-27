# Problem 1. The sock drawer

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

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

# Search for values of red/black that satisfy the requirements
#   of the problem
def search_values():
    print('\nblack  red  disc.     prob.')
    for b in range(1,51):
        prob = math.sqrt(8*b*b+1)
        red = math.ceil((math.sqrt(2)+1)*b)
        half = (red/(red+b))*((red-1)/(red-1+b))
        print('{:5d}'.format(b),'{:4d}'.format(red),
              '{:6.2f}'.format(prob),'{:9.6f}'.format(half))



simulate()
search_values()
