# Problem 28. Catching the greedy counterfeiter

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def probability_exact(squares, cells):
    return math.comb(squares,cells)    * \
           math.pow(cells/squares, cells) * \
           math.pow((squares-cells)/squares, squares-cells)

def check_cells(squares, cells):
    exactly = 0
    # Probability is number of cells per square   
    prob = cells / squares

    for i in range(n):
        count_cells = 0
        for j in range(squares):
            if random.random() <= prob:
                count_cells += 1

        # Check if exact number of cells counted
        if count_cells == cells:
            exactly += 1

    print('Probability of exactly {:2d} microbes  = {:.4f}'.
          format(cells, probability_exact(squares, cells)))
    print('Proportion of exactly  {:2d} microbes  = {:.4f}'.
          format(cells, exactly/n))

def simulate():
    # i squares, j cells
    for i in [20,100]:
        print('For {:3d} squares:'.format(i))
        for j in [3,5]:
            check_cells(i, j)

simulate()
