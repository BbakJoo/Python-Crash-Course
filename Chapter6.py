# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 03:09:58 2018

@author: Ju-Un Park
"""

# Dictionaries
alien_0 = {'color': 'green', 'points' : 5}

print(alien_0['color'])
print(alien_0['points'])

# Working with Dictionaries
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'color': 'yellow'}
print("The alien is now " + alien_0['color'] + ".")

### More
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position : " + str(alien_0['x_position']))

    # Move the alien to the right
    # Determine how far to move the alien basd on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))


# Removing Key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# A dictionary of similar objects
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

print("Sarah's favorite language is " + 
      favorite_languages['sarah'].title() + 
      ".")

# 6-1
person = {
        'first_name': 'John',
        'last_name': 'Park',
        'age' : 33,
        'city' : 'Seattle',
        }
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2
favorite_numbers = {
        'john' : 3,
        'nick' : 12,
        'tom' : 52,
        'jen' : 7,
        }

for name in favorite_numbers:
    print(name.title() + "'s favorite number is " + str(favorite_numbers[name]) + ".")

# 6-3
glossary = {
        'len()': 'length of list',
        'strip()': 'remove the spaces',
        'print()': 'print the string',
        }

for word in glossary:
    print(word +": " + glossary[word]+ "\n")


# Looping through a dictionary
user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
        }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

 # more
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
          language.title() + ".")
    
# looping through all the keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
    

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
    
# looping through all values in a dictionary

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    

# using set to exclude repeat values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 6-4
glossary = {
        'len()': 'length of list',
        'strip()': 'remove the spaces',
        'print()': 'print the string',
        }

for word in glossary:
    print(word +": " + glossary[word]+ "\n")

# 6-5
rivers = {
        'nile': 'egypt',
        'han' : 'korea',
        'yangtze': 'china',
        'mississippi' : 'usa',
        'amazon' : 'brazil',
        }

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
    
for river in rivers.keys():
    print(river)
    
for country in rivers.values():
    print(country)
    
# 6-6
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

names = ['nick', 'sarah', 'park', 'tom', 'david', 'phil']

for name in names:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take the poll.")
        
    
# Nesting
# List of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
    
# A list of dictionaries
    
    # make an empty list for storing aliens
aliens = []

    # make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
    # show the first 5 aliens
for alien in aliens [:5]:
    print(alien)
print("...")

    #show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


# List in a dictionary

    #store information about a pizza being ordered.
pizza = {
        'crust' : 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }
    # summarize the order
print("Your ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza ['toppings']:
    print("\t" + topping)



favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# A dictionary in a dictionary
users = {
        'aeinstein': {
                'first': 'albert',
                'last': 'einstein',
                'location': 'princeton',
                },
        'mcurie': {
                'first': 'marie',
                'last': 'curie',
                'location': 'paris',
                },
        }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# 6-7
person_1 = {
        'first_name': 'John',
        'last_name': 'Park',
        'age' : 33,
        'city' : 'Seattle',
        }
person_2 = {
        'first_name': 'Nick',
        'last_name': 'Kim',
        'age': 35,
        'city': 'Los Angeles',
        }
person_3 = {
        'first_name': 'Jennifer',
        'last_name': 'Oh',
        'age': 32,
        'city': 'New York',
        }

people = [person_1, person_2, person_3]

for person in people:
    print(person['first_name'] + " " + person['last_name'] + " is " +
          str(person['age']) + " years old and lives in " + 
          person['city'] + ".")
    
# 6-8
ggami = {
        'name': 'ggami',
        'kind': 'dog',
        'owner_name': 'John',
        }
bori = {
        'name': 'bori',
        'kind': 'cat',
        'owner_name': 'Nick',
        }
tomi = {
        'name': 'tomi',
        'kind': 'pig',
        'owner_name': 'Jennifer',
        }

pets = [ggami, bori, tomi]

for pet in pets:
    print(pet['name'].title() + " is the " + pet['kind'] + " owned by " + pet['owner_name'].title() + ".")


# 6-9
favorite_places = {
        'john': ['seoul'],
        'tom': ['honolulu', 'new york'],
        'lin': ['los angeles', 'berlin', 'london'],
        }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places:")
    for place in places:
        print("\t" + place.title())
    
# 6-10
favorite_numbers = {
        'john' : [3, 7, 21],
        'nick' : [12, 54],
        'tom' : [52, 20, 99],
        'jen' : [32, 12, 7],
        }

for name, numbers in favorite_numbers.items():
    print('\n' + name.title() + "'s favorite number:")
    for number in sorted(numbers):
        print("\t" + str(number))
        
        
# 6-11
cities = {
        'seattle': {
                'population': 704358,
                'state': 'washington',
                'capita': 55184,
                },
        'new york': {
                'population': 8537673,
                'state': 'new york',
                'capita': 35508,
                },
        'los angeles': {
                'population': 3976324,
                'state': 'california',
                'capita': 31619,
                },
        }

for city, information in cities.items():
    print("\nThese are information about " + city.title() + ":")
    print("\tpululation: " + str('{:,}'.format(information['population'])))
    print("\tstate: " + information['state'].title())
    print("\tcapita: " + str('{:,}'.format(information['capita'])))
        
