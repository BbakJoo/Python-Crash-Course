# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:23:01 2018

@author: Ju-Un Park
"""

import json

import pygal_maps_world

from country_codes import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
    
# Build a dictionary of population data.
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_population[code] = population

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')