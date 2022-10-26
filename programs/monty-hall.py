# Simulation of Monty Hall problem
# Moti Ben-Ari

import random, math

# Number of simulations
n = 10000

def simulate():
    wins_stay   = 0   # Count of games won by staying
    wins_change = 0   # Count of games won by changing

    # doors: False for goat, True for car
    for i in range(n):
        doors = [False, False, False]
        car = random.randint(1,3)
        doors[car-1] = True

        # Wlog contestant chooses door 0
        if doors[0]:
            wins_stay += 1
        else:
            wins_change += 1

    print('Wins when staying with original door = {:.4f}'.
          format(wins_stay / n))
    print('Wins when changing door              = {:.4f}'.
          format(wins_change / n))

simulate()
