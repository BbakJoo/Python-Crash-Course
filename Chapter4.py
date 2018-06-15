# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:13:32 2018

@author: Ju-Un Park
"""

# Looping through an entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    
# More work with for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


# Doing something after a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

# Avoid indentation error
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# Do not forget colon and indentation

# 4-1
pizzas = ['combo', 'cheese', 'hawaiian']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
    
print("I really love pizza!")

# 4-2
animals = ['dog', 'cat', 'pig']
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")

# Making numerical lists
# using range() function

for value in range(1,6):
    print(value)
    
# using range() to make a list of numbers

numbers = list(range(1,6))
print(numbers)

# Even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

# Squares
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

#simple statistics
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

#list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# 4-3
for i in range(1,21):
    print(i)

# 4-4
million = list(range(1,1000001))
    
# 4-5
min(million)
max(million)
sum(million)

# 4-6
for i in range(1,21,2):
    print(i)

# 4-7
for i in range(3,31,3):
    print(i)

# 4-8
for i in range(1,11):
    print(i**3)
    
# 4-9
cubes = [i**3 for i in range(1,11)]


# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    
# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# This does not work
friend_foods = my_foods #updating my foods will update friend foods and vice versa

# 4-10
items = ['car', 'cycle', 'ski', 'board', 'tumbler', 'mic']
print(items[0:3])
print(items[2:5])
print(items[-3:])

# 4-11
pizzas = ['combo', 'cheese', 'hawaiian']
friend_pizzas = pizzas[:]

pizzas.append("pepperoni")
friend_pizzas.append("Potato")

print(pizzas)
print(friend_pizzas)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)

# Tuples Can't be modified (immutable)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
# 4-13
buffet_foods = ('sushi', 'kimchi', 'dimsum', 'tea', 'fruit')
for food in buffet_foods:
    print(food)
    
buffet_foods[0] = 'roll'

buffet_foods = ('pizza', 'burger', 'dimsum', 'tea', 'fruit')
for food in buffet_foods:
    print(food)
    
    
