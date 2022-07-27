# Problem 56. Molina's urn

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def draw(w1, w2, b2):
    m = w2 + b2
    all_white_1 = 0
    all_white_2 = 0
    all_black_2 = 0

    for i in range(n):
        # Two draws from urn 1
        color_u1_1 = random.randint(1, m)
        color_u1_2 = random.randint(1, m)
        # Two draws from urn 2
        color_u2_1 = random.randint(1, m)
        color_u2_2 = random.randint(1, m)

        # Did we draw two white from urn 1?
        if color_u1_1 <= w1 and color_u1_2 <= w1:
            all_white_1 += 1
        # Did we draw two white from urn 2?
        if color_u2_1 <= w2 and color_u2_2 <= w2:
            all_white_2 += 1
        # Did we draw two black from urn 1?
        if color_u2_1 >  w2 and color_u2_2 >  w2:
            all_black_2 += 1

    print('For w1 = {:d}, w2 = {:d}, b2 ={:d}:'.
          format(w1, w2, b2))
    print('Proportion of two whites in urn 1          = {:.4f}'.
          format(all_white_1 / n))
    print('Proportion of two whites or black in urn 2 = {:.4f}'.
          format((all_white_2 + all_black_2) / n))

def simulate():
    draw(10, 6, 8)
    draw(17, 8, 15)
    draw(29, 20, 21)
    draw(65, 33, 56)

simulate()
