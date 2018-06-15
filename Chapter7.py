# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:57:58 2018

@author: Ju-Un Park
"""

# User input and while loops

# how the input() function works

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing clear prompts

name = input("Please enter your name: ")
print("Hello, " + name + "!")

###

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")


# Using int() to accept numerical input

age = input("How old are you? ")

age = int(age)
age >= 18

###
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    
# Modulo operator
4 % 3 # 1
5 % 3 # 2
6 % 3 # 0

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


# 7-1
car = input("What kind of car would you like to rent?")
print("Let me see if I can find you a " + car.title())

# 7-2
number = input("How many people are in your dinner group?")
number = int(number)

if number < 8:
    print("Your table is ready.")
else:
    print("You'll have to wait for a table.")
    

# While loop
    
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    

# Letting the user choose when to quit
    
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        
# Using a flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
        
    else:
        print(message)
        
# Using break to exit a loop
        
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")


# Using continue in a loop
    
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)
    
# Avoiding infinite loops
    
    # This loop runs forever
    
x = 1
while x <= 5:
    print(x)
    

# 7-4
prompt = "\nPlease enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are done.) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print("I will add " + topping + " to you pizza.")
        
# 7-5
prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are done.) "

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    else:
        try:
            age = int(age)
            if age > 0:
                goodinput = True
                if age < 3:
                    print("The ticket is free.")
                elif 3 <= age <= 12:
                    print("The ticket is $10.")
                elif age > 12:
                    print("The ticket is $15.")
            else:
                print("You have entered wrong number. Try again. ")
        except ValueError:
            print("Please enter the number.")

        
# 7-6
prompt = "\nPlease enter the pizza toppings you want to add:"
prompt += "\n(Enter 'quit' when you are done.) "

active = True
while active:
    topping = input(prompt)
    
    if topping != 'quit':
        print("I will add " + topping + " to you pizza.")
    else:
        active = False

# 7-7
x = 1

while x < 3:
    print(x)
    

# Using a while looop with lists and dictionaries
    
# Moving items from one list to another
    
    # Start with users that need to be verified.
    # and an empty list to hold confirmed users.
    
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

    # Verify each user until there are no more unconfirmed users.
    # Move each verified user into the list of confirmed users.
    
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
    # Display all confirmed users.
print("\nThe follwing users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
# Removing all instances of specific values from a list
    
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# Filling a dictionary with user input

responses = {}

    # Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the preson's name and response.
    name = input("\nWhat is your name?")
    response = input("Which moutain would you like to climb someday? ")
    
    # Store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
    # Polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to climb " + response + ".")
        

# 7-8
sandwich_orders = ['BBQ', 'Cajun', 'Philly Steak', 'Spicy Chicken', 'Pulled Pork']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = (sandwich_orders.pop(0))
    print("I made your " + current_sandwich + " sandwich.")
    
    finished_sandwiches.append(current_sandwich)
  
print("\nFinished sandwiches: ")
    
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
# 7-9
sandwich_orders = ['BBQ', 'pastrami', 'Cajun', 'Philly Steak', 'pastrami',  'Spicy Chicken', 'Pulled Pork', 'pastrami']
finished_sandwiches = []

print ("Sorry, our deli has run out of pastrami.\n")

while sandwich_orders:
    current_sandwich = (sandwich_orders.pop(0))
    if current_sandwich == 'pastrami':
        del current_sandwich
    else:
        print("I made your " + current_sandwich + " sandwich.")

        finished_sandwiches.append(current_sandwich)
        
print("\nFinished sandwiches: ")
    
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    
# 7-10
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    place = input ("\nIf you could visit one place in the world, where would you go? ")
    
    responses[name] = place
    
    repeat = input("Would you like to take another poll? ")
    
    if repeat == 'no':
        polling_active = False
        
    for name, place in responses.items():
        print(name.title() + "'s dream place in the world is " + place + ".")
        
