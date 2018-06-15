# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 21:39:41 2018

@author: Ju-Un Park
"""

#List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#3-1
names = ['John', 'Eric', 'Tom', 'Dan', 'Nick']
print(names[0])
print(names[1])

#3-2
print(names[0] + " is one of my friend.")
print(names[1] + " is one of my friend.")
print(names[2] + " is one of my friend.")
print(names[3] + " is one of my friend.")
print(names[4] + " is one of my friend.")

#3-3
transportation = ['bus', 'taxi', 'train',]
print("I would like to own a " + transportation[0])

# List modifications
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #modify element of list
print(motorcycles)

# append elements to the end of the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# another append
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

# inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing an item using the del statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# another
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# removing an item using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()  #pop the last element
print(motorcycles)
print(popped_motorcycle)

# Another pop()
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Popping items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# Another removing
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 3-4
guest = ['Eric', 'Mike', 'Thomas']
print("Hi, " + guest[0] + ". You are invited to dinner party.")

# 3-5
print("Sorry to say that " + guest.pop(0) + " can not make to party")

guest.insert(0, 'Nick')
print("However, " + guest[0] + " was invited to dinner.")

# 3-6
guest.insert(3, 'Dan')
guest.insert(4, 'Jessica')
guest.append('Rachel')

# 3-7
guest.pop()
print("Hi, " + guest.pop() + ". Sorry to say that the dinner party is canceled.")

del guest[0]

# Sorting a list with sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #alphabetical sort
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #reverse alphabet sort
print(cars)

# Sorting a list temporarily with sorted()

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse() # not sort reverse alphabetically, just backward list
print(cars)

# Finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

# 3-8
world = ['Vietnam', 'China', 'Japan', 'Korea', 'Nepal', 'Mexico']
print(sorted(world))
print(world)
print(sorted(world, reverse = True))
print(world)
world.reverse()
print(world)
world.reverse()
print(world)
world.sort()
print(world)
world.sort(reverse=True)
print(world)

# 3-9
print("There are " + str(len(world)) + " countries that I want to visit.")
