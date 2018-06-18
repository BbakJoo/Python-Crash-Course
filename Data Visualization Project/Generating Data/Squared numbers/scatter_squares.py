# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:56:19 2018

@author: Ju-Un Park
"""


import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight') # save the plot to file.

plt.show()
