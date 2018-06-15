# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 20:50:23 2018

@author: Ju-Un Park
"""

#Context

print("Hello Python world!")

message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

#2-1
hello = "Hello, How are you?"
print(hello)

#2-2
hello = "Hello, How are you?"
print(hello)

hello = "Hi, How are you?"
print(hello)

# Apostrophe
message = "One of Python's strength is its diverse community."
print(message)

#this gives error
mssage = 'One of Python's strength is its diverse community.' 

#2-3
name = "Ju-Un Park"

print("Hello " + name + ", would you like to learn some Python today?")

#2-4
name = "ju-un park"
print(name.upper())
print(name.lower())
print(name.title())

#2-5,6
famous_name = "albert einstein"
message = "A person who never made a mistake never tried anything new."

print(famous_name.title() + ' once said, "' + message + '"')

#2-7
name = ' \n\tJu-un Park '
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())

#context
name = "ada lovelace"
print(name.title())

###
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

###
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

###
print("hello, " + full_name.title() + "!")

###
message = "Hello, " + full_name.title() + "!"
print(message)

###
print("Python")

print("\tPython") #add tab \t

print("Languages:\nPython\nC\nJavaScript") #add new line \n

print("Languages:\n\tPython\n\tC\n\tJavaScript")

###
favorite_language = "python "

favorite_language

favorite_language.rstrip() #rstrip = no space on right side of string

###
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip() #lstrip = no space on left side of string
favorite_language.strip() #strip = strip space on both side


#gives type error
age = 23
message = "Happy " + age + "rd Birthday!"

print(message)

#correct one
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)

#2-8
print(5+3)
print(10-2)
print(2*4)
print(2**3)
print(40/5)

#2-9
favorite_number = 7
print(str(favorite_number) + " is my favorite number")

# Say hello to everyone.
print("Hello python people!")

#2-10
# This is comment line

#2-11
import this