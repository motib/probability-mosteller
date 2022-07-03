# Problem 21. Should you sample with or without replacement?

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

# Three simulations
# For the second urn with/without replacement
#   doesn't matter

def simulate_with_replacement():
    success = 0
    for i in range(n):

        # Select random urn: A is 0, B is 1
        urn = random.randint(0,1)

        # Select balls: 1 and 2 are red, 3 is green
        if urn == 0:
            first_ball  = random.randint(1,3)
            # Urn a: with replacement so still (1,3)
            second_ball = random.randint(1,3)
        else:
            # Urn B: probability 1/2 for both red and green
            first_ball  = random.randint(2,3)
            second_ball = random.randint(2,3)

        # Two red balls: success if urn A
        if first_ball != 3 and second_ball != 3:
            if urn == 0:
                success += 1
        # Otherwise: success if urn B
        else:
            if urn == 1:
                success += 1
        
    print('Expectation of winning = 0.5972')
    print('Average wins           = {:.4f}'.\
          format(success/n))

def simulate_without_replacement():
    success = 0
    for i in range(n):

        # Select random urn: A is 0, B is 1
        urn = random.randint(0,1)
        # Select balls: 1 and 2 are red, 3 is green
        if urn == 0:
            first_ball  = random.randint(1,3)
            # Urn A: sample without replacement
            if first_ball == 1 or first_ball == 2:
                # If first ball red, second is red or green
                second_ball = random.randint(2,3)
            else:
                # Otherwise, second is one of the reds
                second_ball = random.randint(1,2)
        else:
            # Urn B: probability 1/2 for both red and green
            first_ball  = random.randint(2,3)
            second_ball = random.randint(2,3)

        # Two green balls: success if urn B
        if first_ball == second_ball == 3:
            if urn == 1:
                success += 1
        # Otherwise: success if urn A
        else:
            if urn == 0:
                success += 1
        
    print('Expectation of winning = 0.6250')
    print('Average wins           = {:.4f}'.\
          format(success/n))

def simulate_decide_replacement():
    success = 0
    for i in range(n):

        # Select random urn: A is 0, B is 1
        urn = random.randint(0,1)
        # Select balls: 1 and 2 are red, 3 is green
        if urn == 0:
            first_ball  = random.randint(1,3)
            # Urn A: if first ball is red
            if first_ball == 1 or first_ball == 2:
                # Sample with replacement
                second_ball = random.randint(1,3)
            # Urn A: If first ball is green
            else:
                # Sample without replacement
                second_ball = random.randint(2,3)
        else:
            # Urn B: probability 1/2 for both red and green
            first_ball  = random.randint(2,3)
            second_ball = random.randint(2,3)

        # If urn A: success if two reds or
        #   first green and second red
        if urn == 0:
            if (first_ball == 1 and second_ball == 2) or \
                first_ball == 3 and \
                    (second_ball == 1 or second_ball == 2):
                success += 1
        # Otherwise: success for urn B
        else:
                success += 1
        
    print('Expectation of winning = 0.6389')
    print('Average wins           = {:.4f}'.\
          format(success/n))

print('With replacement:')
simulate_with_replacement()

print('Without replacement:')
simulate_without_replacement()

print('Decide after first draw:')
simulate_decide_replacement()
