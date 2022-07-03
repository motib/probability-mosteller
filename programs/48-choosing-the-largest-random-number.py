# Problem 48. Choosing the largest random number

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random, math

# Number of simulations
n = 10000

def prob_win(d):
    return 1/3 + d/2 + d**2/1 - 3*d**3/2

def guess_largest(cards, indifference):
    successes = 0

    for i in range(n):
        # Create list of cards and shuffle
        bins = [random.random()
                for c in range(cards) if True]
        random.shuffle(bins)

        # Get index of largest value
        largest_index = bins.index(max(bins))

        # Index of first element greater than
        #   indifference value
        # -1 to flag no such elements
        indifference_index = -1
        for j in range(cards):
            if bins[j] > indifference:
                indifference_index = j
                break

        # Search for first card after indifference_index
        #   greater than indifference value 
        # Sentinel for search
        selected_card = cards-1
        largest_so_far = bins[0]

        # If all values <= indifference,
        #   sentinel (last card) is selected
        if indifference_index == -1:
            pass
        # Select first card greater than those
        #   in 0..indifference_index-1
        else:
            # If indifference_index is last card,
            #   select it
            if indifference_index == cards-1:
                selected_card == cards-1
            else:
                # Find largest in range 0..indifference_index-1
                if indifference_index == 0:
                    largest_so_far = 0
                else:
                    largest_so_far = max(bins[0:indifference_index])
                # Search from indifferent_index+1 to end
                #   to find larger element
                # Otherwise sentinel is selected
                for j in (indifference_index,cards):
                    if bins[j] > largest_so_far:
                        selected_card = j
                        break

        if selected_card == largest_index:
            successes += 1

    print('Indifference value = {:.4f}'.
          format(indifference))
    print('Probability of win = {:.4f}'.
          format(prob_win(indifference)))
    print('Proportion of wins = {:.4f}'.
          format(successes/n))

def simulate():
    cards = 3
    print('For {:2d} cards:'.format(cards))
    for c in [.6, (1+math.sqrt(6))/5, .72]:
        guess_largest(3, c)

simulate()
