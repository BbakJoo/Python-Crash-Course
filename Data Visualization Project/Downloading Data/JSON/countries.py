# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:30:54 2018

@author: Ju-Un Park
"""

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])