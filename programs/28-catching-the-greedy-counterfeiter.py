# Problem 28. Catching the greedy counterfeiter

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def expectation_all_real(boxes, bad, drawn):
    return math.comb(boxes, drawn)    * \
           math.pow(bad/boxes, drawn) * \
           math.pow((boxes-bad)/boxes, boxes - drawn)

def check_coins(boxes, bad, drawn):
    all_real = 0
    for i in range(n):

        # Draw from each box
        # Arbitrarily assume that first "bad" coins
        #   are counterfeit
        counterfeit = 0
        for j in range(boxes):
            if random.randint(1,boxes) <= bad:
                counterfeit += 1

        # Check if counterfeit drawn
        if counterfeit == drawn:
            all_real += 1

    print('For {:2d} bad coins, {:2d} draws:'.
          format(bad, drawn))
    print('Probability of counterfeit  = {:.4f}'.
          format(expectation_all_real(boxes, bad, drawn)))
    print('Proportion counterfeit      = {:.4f}'.
          format(all_real/n))

def simulate():
    print('For 20 boxes:\n')
    # Tuple is (boxes, coins, drawn)
    for i in [(20,10,2), (20,10,8), (20,5,2), (20,5,4)]:
        check_coins(i[0], i[1], i[2])
 
# Limit according to Mosteller's derivation
#   of the Poisson distribution
def limit(bad, drawn):
    return (math.e**(-bad) * bad**drawn) / \
        math.factorial(drawn)

# Compare limit and binomial computation of p for
#   increasing n
def limit_of_probability():
    print()
    bad = 10
    drawn = 8
    for n in (100, 1000, 10000, 1000000):
        print('Limit = {:.8f}'.format(limit(bad,drawn)) +
              ', binomial = {:.8f}'.
            format(expectation_all_real(n, bad, drawn)) +
              ', n = {:d}'.format(n))

simulate()
limit_of_probability()
    