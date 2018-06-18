# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 00:35:05 2018

@author: Ju-Un Park
"""

#Choose any location you’re interested in, and make a visualization that plots its rainfall.
#Start by focusing on one month’s data, and then once your code is working, run it for a full year’s data.

import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)
        
    
"""    
    # print index number and header
    for index, column_header in enumerate(header_row):
        print(index, column_header)
"""
    
# Plot data.
fig = plt.figure(dpi=124, figsize=(10, 6))
plt.plot(dates, rainfalls, c='blue', alpha=0.75)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)

# Format plot.
title = "Daily rainfalls - 2014\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()