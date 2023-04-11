# Problem 22. The ballot box

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random

# Number of simulations
n = 10000

def count_votes(a, b):
    successes = 0
    for i in range(n):

        votes_a = votes_b = 0
        for votes_ab in range(a+b):
            # If all votes for A counted, enter vote for B
            if votes_a == a:
                votes_b += 1
            # If all votes for B counted, enter vote for A
            elif votes_b == b:
                votes_a += 1
            # Otherwise, enter random vote
            else:
                # Compute the probability of a vote for A
                #   from the remaining A votes (a-votes_a)
                #   divided by the remaining votes (a+b-votes_ab)
                prob_a = (a-votes_a) / (a+b-votes_ab)
                if random.random() < prob_a:
                    votes_a += 1
                else:
                    votes_b += 1

            # Success if equal votes
            if votes_a == votes_b:
                successes += 1
                break

    print('For a = {:2d}, b = {:2d}:'.format(a,b))
    print('Probability of a tie = {:.4f}'.\
           format(2*b / (a+b)))
    print('Proportion of ties   = {:.4f}'.\
           format(successes / n))

def simulate():
    # Tuple is (votes for A, votes for B)
    for votes in [(3,2), (20,18), (20,8)]:
        count_votes(votes[0], votes[1])

simulate()
