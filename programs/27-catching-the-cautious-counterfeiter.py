# Problem 27. Catching the cautious counterfeiter

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def expectation_all_real(n):
    return math.pow((n-1)/n, n)

def check_coins(boxes):
    all_real = 0
    for i in range(n):

        # Draw a random coin from each box of n
        # The value 1 is arbitrarily counterfeit
        counterfeit = False
        for j in range(boxes):
            if random.randint(1,boxes) == 1:
                counterfeit = True
                break

        if not counterfeit:
            all_real += 1

    print('For {:3d} boxes:'.format(boxes))
    print('Probability of all real = {:.4f}'.
          format(expectation_all_real(boxes)))
    print('Proportion all real     = {:.4f}'.
          format(all_real/n))

def simulate():
    # Check for various boxes and coins
    for i in [10, 100, 200]:
        check_coins(i)

simulate()
