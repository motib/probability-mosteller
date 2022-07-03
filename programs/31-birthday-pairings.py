# Problem 31. Birthday pairings

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

# Compute the probability of no birthday pair
def probability_no_pair(r):
    return math.factorial(365) / (math.factorial(365-r) * (365**r))

# For k persons compute average number
#   of random choices of k birthdays
#   that have no pairs
def average_no_pairs(k):
    birthdays = 365
    no_pairs = 0

    for i in range(n):
        # List for storing birthdays selected so far
        bins = [] 
        found_pair = False

        for j in range(k):
            new_birthday = random.randint(1,365)
            # If new birthday in list a pair has been found
            if new_birthday in bins:
                found_pair = True
                break
            # Otherwise, append it to list
            else:
                bins.append(new_birthday)

        if found_pair:
            no_pairs += 1
    
    print('Probability of no pairs = {:.4f}'.\
        format(probability_no_pair(k)))
    print('Proportion of no pairs        = {:.4f}'.\
        format(1.0-(no_pairs/n)))

def simulate():
    for k in range(21,26):
        print('For {:2d} people:'.format(k))
        average_no_pairs(k)

simulate()
