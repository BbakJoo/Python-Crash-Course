# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 01:41:32 2018

@author: Ju-Un Park
"""

from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """ Return the pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If the country wasn't found, return None.
    return None

print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))

