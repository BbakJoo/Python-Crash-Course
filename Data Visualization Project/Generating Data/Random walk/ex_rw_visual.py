# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 21:22:56 2018

@author: Ju-Un Park
"""

import matplotlib.pyplot as plt

from ex_random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk() # Increase value of num_points to 50000 from 5000(set value)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))
    
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=20)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break