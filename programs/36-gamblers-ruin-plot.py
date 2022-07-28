# Problem 36. Gambler's ruin plot

# Copyright 2022. Moti Ben-Ari
# Creative Commons Attribution-ShareAlike

# Interactive input of parameters m, n, p
# Close the plot window to continue

import random
import numpy as np
import matplotlib.pyplot as plt

# Uncomment here and in plotpoints() for TikZ/PGF output
#import tikzplotlib

# Number of steps to plot
steps = 150

# Initialize arrays for data to plot
x = np.arange(steps+1)
y = np.zeros(steps+1)

# Default locations of m and n
m = 20
n = 50
# Default probability of a step to the right
p = 0.67

# Interactive input of parameters (or use default)
def get_parameters():
    global m, n, p
    while True:
        default = input("Use default parameters m, n, p? (y[es], n[o], q[uit]) ")
        if default == 'q':
            quit()
        elif default == 'y':
            return
        elif default == 'n':
            while True:
                m = int(input("Initial position m: "))
                if m < 0:
                    print('Error: m must be >= 0')
                    continue
                n = int(input("Upper limit n: "))
                if n < m:
                    print('Error: n must be >= m')
                    continue
                p = float(input("Probability of right step: "))
                if p < 0 or p > 1:
                    print('Error: p must be >= 0 and <= 1')
                    continue
                return

def plot_points():
    plt.title("Gambler's ruin for m = {:d}, n = {:d}, p = {:.2f}".
              format(m, n, p))
    plt.xlabel('Steps')
    plt.ylabel('Position')
    plt.ylim(0, n+1)
    plt.xticks(np.arange(0, steps+1, 20))
    plt.yticks(np.arange(0, n+3, 4))

    plt.plot(x, y)
    #tikzplotlib.save("../en/36-gamblers-ruin-plot.tex")
    plt.show()

def simulate_gamble():
    global x, y
    current = m
    for s in range(steps+1):
        # If reached zero or n don't take a step
        if current != 0 and current != n:
            if random.random() < p:
                current += 1
            else:
                current -= 1
        y[s] = current

def main():
    while True:
        get_parameters()
        simulate_gamble()
        plot_points()

main()
