# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:57:14 2018

@author: Ju-Un Park
"""

# IF Statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
# Checking for equality
car = 'bmw'
car == 'bmw'

car = 'audi'
car == 'bmw'

# Ignoring case when checking for equality
car = 'Audi'
car == 'audi'

car = 'Audi'
car.lower() == 'audi'

car = 'Audi'
car.lower() == 'audi'

car

# Checking for inequality

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
# Numerical Comparisons
age = 18
age == 18

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21
age <= 21
age > 21
age >= 21

# Checking Multiple conditions

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 #both should be true to give True

age_1 = 22
age_0 >= 21 and age_1 >= 21

(age_0 >= 21) and (age_1 >= 21) # improve readability

# Using or to check multiple conditions

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21 #both should fail to give False

age_0 = 18
age_0 >= 21 or age_1 >= 21

# Checking a value is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

# Checking whether a value is not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Boolean Expressions
game_active = True
can_edit = False

# 5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
    
# if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
    
    
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
    
print("Your admission cost is $" + str(price) + ".")

# using multiple elif blocks
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("Your admission cost is $" + str(price) + ".")

# Omitting the else Block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
    
print("Your admission cost is $" + str(price) + ".")

# Testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

 # not working properly when using elif
 requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

# 5-3
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You just earned 5 points")
    
# 5-4
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You just earned 5 points")
else:
    print("You just earned 10 points")

# 5-5
alien_color = ['green', 'yellow', 'red']
if 'green' in alien_color:
    print("You just earned 5 points")
if 'yellow' in alien_color:
    print("You just earned 10 points")
if 'red' in alien_color:
    print("Your just earned 15 points")

# 5-6
age = 5
if 2 > age:
    life = 'baby'
elif 2 <= age < 4:
    life = 'toddler'
elif 4 <= age < 13:
    life = 'kid'
elif 13 <= age < 20:
    life = 'teenage'
elif 20 <= age < 65:
    life = 'adult'
else:
    life = 'elder'
    
print("The person is a " + life + ".")

# 5-7
fruits = ['banana', 'kiwi', 'watermelon', 'apple', 'peach']
favorite_fruits = ['mango', 'orange', 'peach']

if 'mango' in fruits:
    print("You really like mango.")
if 'orange' in fruits:
    print("You really like orange.")
if 'peach' in fruits:
    print("You really like peach.")
 
# Using If statements with lists    
# Checking for special items
    
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# checking that a list is not empty

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    

#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

# 5-8
usernames = ['bbakjoo', 'admin', 'faker', 'mata', 'froja']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else: 
        print("Hello " + username + ", thank you for logging in again.")

# 5-9
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else: 
            print("Hello " + username + ", thank you for logging in again.")
else:
    print("We need to find some users!")
    
# 5-10
current_users = ['Bbak', 'dang', 'fakes', 'ZEDI', 'holi']
new_users = ['daNg', 'zodiac', 'light', 'Zedi', 'lapun']
for user in new_users:
    if user.lower() in [user.lower() for user in current_users]:
        print("Username " + user + " is already taken. You need to enter a new username.")
    else:
        print("Username " + user + " is available.")
    
# 5-11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")