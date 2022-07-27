# Problem 36. Gambler's ruin plot

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

import random
import numpy as np
import matplotlib.pyplot as plt

# Number of steps to plot
steps = 150

# Initialize arrays for data to plot
x = np.arange(steps+1)
y = np.zeros(steps+1)

# Default locations of m and n
m = 20
n = 50
# Default probability of a step to the right
prob = 0.67

# Interactive input of parameters (or use default)
def get_parameters():
    global m, n, prob
    default = input("Use default parameters m, n, p? (Y/N)")
    if default != 'Y' and default != 'y':
        pass
    else:
        print(default)
        m = int(input("Initial position m: "))
        n = int(input("Upper limit n: "))
        prob = float(input("Probability of right step: "))

def plot_points():
    plt.title("Gambler's ruin for m = {:d}, n = {:d}, p = {:.2f}".
              format(m, n, prob))
    plt.xlabel('Steps')
    plt.ylabel('Position')
    plt.ylim(0, n+1)
    plt.xticks(np.arange(0, steps+1, 20))
    plt.yticks(np.arange(0, n+3, 4))

    plt.plot(x, y)
    # Comment out for PGF output
    plt.show()

def simulate_gamble():
    global x, y
    current = m
    for s in range(steps+1):
        # If reached zero or n don't take a step
        if current != 0 and current != n:
            if random.random() < prob:
                current += 1
            else:
                current -= 1
        y[s] = current

def main():
    get_parameters()
    simulate_gamble()
    plot_points()

main()

# Uncomment for tikz output
# import tikzplotlib
# tikzplotlib.save("../en/36-gamblers-ruin-plot.tex")
