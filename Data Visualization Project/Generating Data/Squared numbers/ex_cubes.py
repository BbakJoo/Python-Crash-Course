# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:18:18 2018

@author: Ju-Un Park
"""

# Exercise : Create plot with cube numbers

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 5500, 0, 125000000000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
