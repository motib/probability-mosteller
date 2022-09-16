# Simulation of Monty Hall problem
# Moti Ben-Ari

import random, math

def check_random(games):
    # Count of door where car is: 1s, 2s, 3s 
    ones = twos = threes = 0
    for g in range(games):
        car = random.randint(1,3)
        if car == 1: ones += 1
        if car == 2: twos += 1
        if car == 3: threes += 1
    print('Games = {:d}'.format(games))
    print('Ones = {:.3f}, twos = {:.3f}, threes = {:.3f}'.
          format(ones / games, twos / games, threes / games))
    
def simulate(games):
    wins_stay   = 0   # Count of games won by staying
    wins_change = 0   # Count of games won by changing

    # doors: False for goat, True for car
    for g in range(games):
        doors = [False, False, False]
        car = random.randint(1,3)
        doors[car-1] = True

        # Wlog contestant chooses door 0
        if doors[0]:
            wins_stay += 1
        else:
            wins_change += 1

    print('Games = {:d}'.format(games))
    print('Wins when staying with original door = {:.4f}'.
          format(wins_stay / games))
    print('Wins when changing door              = {:.4f}'.
          format(wins_change / games))

for g in (1000, 10000, 100000):
    check_random(g)
print()
for g in (1000, 10000, 100000):
    simulate(g)
