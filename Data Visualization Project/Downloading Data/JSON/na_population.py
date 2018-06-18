# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 02:00:59 2018

@author: Ju-Un Park
"""

import pygal_maps_world

wm = pygal.maps.world.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_population.svg')

