# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:46:05 2018

@author: Ju-Un Park
"""

# Ch 8 Functions

# Defining a Function

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()


# Passing information to a function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

# 8-1
def display_message(message):
    print("In this chapter, you are learning " + message + ".")
    
display_message("function")

# 8-2
def favorite_book(title):
    print("One of my favorite book is " + title.title() + ".")
    
favorite_book("alice in wonderland")


# Passing Arguments

# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')

# Multiple function calls
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


# Order matters in positional arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

# Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'hamster', pet_name = 'harry')

# Default values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(pet_name='willie')

# Equivalent Function calls
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
    # A dog named Willie.
describe_pet(pet_name='willie')
describe_pet('willie')

    # A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name='harry')

# Argument Errors
describe_pet()


# 8-3
def make_shirt(size, text):
    print("The T-shirt's size is " + size + " and the text " + text + " is printed on it.")
    
make_shirt('small', 'Hello')
make_shirt(text = 'Star Wars', size = 'medium')

# 8-4
def make_shirt(size = 'large', text = 'I love Python'):
    print("The T-shirt's size is " + size + " and the text " + text + " is printed on it.")
    
make_shirt()
make_shirt('medium')
make_shirt(size='small', text='I love R')

# 8-5
def describe_city(city, country):
    print(city.title() + " is in " + country.title() + ".")
    
describe_city('seoul','south korea')


# Return Values

# Returning a simple value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an Augument Optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


# Returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    
###
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
    

# 8-6
def city_country(name, country):
    print('"' + name.title() + ', ' + country.title() + '"')

# 8-7, 8-8
def make_album():
    album = {}
    while True:
        print("\nPlease tell me the name of artist and album title:")
        print("(Enter 'q' at any time to quit)")
        
        a_name = input("Artist: ")
        if a_name == 'q':
            break
        
        a_title = input("Album title: ")
        if a_title == 'q':
            break
        album = {a_name:a_title}
        print(album)
    
# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a list in a function

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

###########
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)    

def show_completed_models(completed_models):
    """show all completed models."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


# 8-9
magician_names = ['Witch', 'Bell', 'Thomas']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magician_names)

# 8-10
magician_names = ['Witch', 'Bell', 'Thomas']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
        
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

       
# 8-11
magician_names = ['Witch', 'Bell', 'Thomas']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    great_magicians = []
    
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
        
    for great_magician in great_magicians:
        magicians.append(great_magician)
        
    return magicians

show_magicians(magician_names)

great_magicians = make_great(magician_names[:])
show_magicians(great_magicians)

show_magicians(magician_names)


# Passing an arbitary number of arguments

def make_pizza(*toppings):
    """ Print the list of toppings that have been requested"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

####
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return(profile)
    
user_profile = build_profile('albert', 'einstein',
                             location= 'princeton',
                             field = 'physics')

print(user_profile)

# 8-12
def sandwiches(*items):
    print("Making a sandwithches with following items:")
    for item in items:
        print("-"+ item)
        
sandwiches('ham')
sandwiches('ham','lettuce','egg')
sandwiches('beef','cheese','lettuce','tomato')

# 8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return(profile)
    
user_profile = build_profile('Ju-Un', 'Park',
                             location= 'University of Washington',
                             field = 'Chemistry')

print(user_profile)

# 8-14
def make_car(manufacturer, name, **car_info):
    """Build a dictionary containing everything we know about a car."""
    car_profile = {}
    car_profile['Manufacturer'] = manufacturer
    car_profile['Model name'] = name
    for key, value in car_info.items():
        car_profile[key] = value
    return(car_profile)
    
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

