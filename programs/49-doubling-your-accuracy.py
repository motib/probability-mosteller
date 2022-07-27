# Problem 49. Doubling your accuracy

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import math, numpy, statistics

# Number of simulations
n = 10000

# Lengths
L1 = 10
L2 = 6
# Variance
variance = 1.0

def simulate():
    # Generate random samples for L1 and L2
    L1_samples = numpy.random.normal(L1, variance, n)
    L2_samples = numpy.random.normal(L2, variance, n)

    # Compute the means, errors from means,
    #   and variances for L1 and L2
    L1_mean = statistics.mean(L1_samples)
    L1_mean_error = abs(L1-L1_mean)
    L2_mean = statistics.mean(L2_samples)
    L2_mean_error = abs(L2-L2_mean)

    L1_var = statistics.variance(L1_samples)
    L2_var = statistics.variance(L2_samples)

    # Generate random samples for L1+L2 and L1-L2
    L_plus  = numpy.random.normal(L1+L2, variance, n)
    L_minus = numpy.random.normal(L1-L2, variance, n)

    # Compute the means, errors from means,
    #   and variances for L1+L2 and L1-L2
    # sd = sum / difference
    L1_better = 0.5*(L_plus+L_minus)
    L2_better = 0.5*(L_plus-L_minus)
    L1_sd_mean = statistics.mean(L1_better)
    L2_sd_mean = statistics.mean(L2_better)
    L1_sd_mean_error = abs(L1-L1_sd_mean)
    L2_sd_mean_error = abs(L2-L2_sd_mean)

    L1_sd_var = statistics.variance(L1_better)
    L2_sd_var = statistics.variance(L2_better)

    print('For L1 = {:d}, L2 = {:d}, variance = {:3.2f}:'.
          format(L1, L2, variance))
    print('Errors of mean:')
    print('    L1 = {:.4f}, L1_sd = {:.4f}'.
          format(L1_mean_error, L1_sd_mean_error))
    print('    L2 = {:.4f}, L2_sd = {:.4f}'.
          format(L2_mean_error, L2_sd_mean_error))
    print('Variances:')
    print('    L1 = {:.4f}, L1_sd = {:.4f}'.
          format(L1_var, L1_sd_var))
    print('    L2 = {:.4f}, L2_sd = {:.4f}'.
          format(L2_var, L2_sd_var))
    
simulate()
