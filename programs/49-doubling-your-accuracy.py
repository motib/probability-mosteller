# Problem 49. Doubling your accuracy

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import math, numpy, statistics

# Number of simulations
n = 10000

def mean_and_variance(L1, L2, variance):
    # Generate random samples for L1 and L2
    L1_samples = numpy.random.normal(L1, variance, n)
    L2_samples = numpy.random.normal(L2, variance, n)

    # Compute the means, errors from means,
    #   and variances for L1 and L2
#     L1_mean = statistics.mean(L1_samples)
# #     L1_mean_error = abs(L1-L1_mean)
#     L2_mean = statistics.mean(L2_samples)
# #     L2_mean_error = abs(L2-L2_mean)
# 
#     L1_var = statistics.variance(L1_samples)
#     L2_var = statistics.variance(L2_samples)

    # Generate random samples for L1+L2 and L1-L2
    L_plus  = numpy.random.normal(L1+L2, variance, n)
    L_minus = numpy.random.normal(L1-L2, variance, n)

    # Compute the means, errors from means,
    #   and variances for L1+L2 and L1-L2
    L1_better = 0.5*(L_plus+L_minus)
    L2_better = 0.5*(L_plus-L_minus)
    L1_mean   = statistics.mean(L1_better)
    L2_mean   = statistics.mean(L2_better)
    L1_var    = statistics.variance(L1_better)
    L2_var    = statistics.variance(L2_better)

    print('For L1 = {:d}, L2 = {:d}, variance = {:3.2f}:'.
          format(L1, L2, variance))
    print('L1 mean = {:.4f}, L1 variance = {:.4f}'.
          format(L1_mean, L1_var))
    print('L2 mean = {:.4f}, L2 variance = {:.4f}'.
          format(L2_mean, L2_var))
    print()
    
def simulate():
    # A tuple is L1, L2, variance
    for t in [(40,16,0.5),(40,16,1.0),(40,16,2.0)]:
        mean_and_variance(t[0], t[1], t[2])

simulate()
