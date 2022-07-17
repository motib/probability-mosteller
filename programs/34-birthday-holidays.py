# Problem 34. Birthday holidays

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def compute_worker_days(workers):
    days = 365
    work_days = 0
    
    for i in range(n):
        # Bin for each day in a year
        # True  = at least one worker has this birthday
        # False = none of the workers have this birthday
        bins = [False] * days

        # For each worker set random birthday True
        for j in range(workers):
            bins[random.randint(0, days-1)] = True

        # Count number of days with no birthdays
        for k in range(days):
            if not bins[k]:
                work_days += 1

    expectation = days * workers * ((days-1)/days) ** workers
    print('Expectation work-days    =  {:5.0f}'.\
           format(expectation))
    print('Average work days        =  {:5.0f}'.\
           format(work_days * workers/n))
    print('Ratio work-days / 365**2 = {:.4f}'.\
           format(expectation/(days * days)))

def simulate():
    for w in [100, 250, 364, 365]:
        print('For {:3d} people'.format(w))
        compute_worker_days(w)

simulate()
