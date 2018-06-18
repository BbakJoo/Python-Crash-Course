# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:26:15 2018

@author: Ju-Un Park
"""
# Exercise : Create a visualization that shows what happens when you roll three D6 dice.

import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies) # ADD results in histogram
hist.render_to_file('three_dice_visual.svg')
