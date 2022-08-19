# Problem 49. Doubling your accuracy

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import math, numpy, statistics

# Number of simulations
n = 10000

def mean_and_variance(L1, L2, variance):
    sd = math.sqrt(variance)

    # Generate random samples for L1 and L2
    L1_samples = numpy.random.normal(L1, sd, n)
    L2_samples = numpy.random.normal(L2, sd, n)

    # Generate random samples for L1+L2 and L1-L2
    L_plus  = numpy.random.normal(L1+L2, sd, n)
    L_minus = numpy.random.normal(L1-L2, sd, n)

    # Compute L1, L2 from L1 +/- L2
    L1_better        = 0.5*(L_plus+L_minus)
    L2_better        = 0.5*(L_plus-L_minus)

    # Compute means and variances for L1+L2 and L1-L2
    L1_better_mean   = statistics.mean(L1_better)
    L2_better_mean   = statistics.mean(L2_better)
    L1_better_var    = statistics.variance(L1_better)
    L2_better_var    = statistics.variance(L2_better)

    print('For L1 = {:d}, L2 = {:d}, variance = {:3.2f}:'.
          format(L1, L2, variance))
    print('L1 mean = {:.4f}, L1 variance = {:.4f}'.
          format(L1_better_mean, L1_better_var))
    print('L2 mean = {:.4f}, L2 variance = {:.4f}'.
          format(L2_better_mean, L2_better_var))
    print()
    
def simulate():
    # A tuple is L1, L2, variance
    for t in [(40,16,0.5),(40,16,1.0),(40,16,2.0)]:
        mean_and_variance(t[0], t[1], t[2])

simulate()
