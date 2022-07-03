# Problem 32. Finding your birthmate

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def simulate_for_k_people(k):
    birthdays = 365      # Number of birthdays
    your_birthday = 365  # Arbitrary choice of your birthday
    no_matches = 0

    for j in range(n):
        found_match = False

        for i in range(k):
            new_birthday = random.randint(1,365)
            if new_birthday == your_birthday:
                found_match = True
                break

        if found_match:
            no_matches += 1

    print('Probability of no match = {:.4f}'.\
          format((364.0/365.0)**k))
    print('Proportion no match     = {:.4f}'.\
          format(no_matches/n))

def simulate():
    for k in range(251, 256):
        print('For {:3d} people:'.format(k))
        simulate_for_k_people(k)

simulate()
