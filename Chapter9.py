# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:27:30 2018

@author: Ju-Un Park
"""

#Chapter 9 CLASSES

# Creating and using a class

# Creating the dog class

class Dog():
    """ A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize anme and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
# Making an instance from a class

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# 9-1

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attribute"""
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        """describing the restaurant"""
        print(self.name.title() + " is the " + self.type.title() + " restaurant.")
        
    def open_restaurant(self):
        """prints a message indicating that the restaurant is open"""
        print(self.name.title() + " is now open!")
        
first_restaurant = Restaurant('Than Brothers', 'vietnamese')
print(first_restaurant.name)
print(first_restaurant.type)

first_restaurant.describe_restaurant()
first_restaurant.open_restaurant()

# 9-2
second_restaurant = Restaurant('Gawon', 'korean')
third_restaurant = Restaurant('red robins', 'american')

second_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()

# 9-3

class User():
    
    def __init__(self, first, last, username, age, email):
        self.first_name = first
        self.last_name = last
        self.username = username
        self.age = age
        self.email = email
        
    def describe_user(self):
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("Age: " + str(self.age))
        print("Email Address: " + self.email)
        
    def greet_uesr(self):
        print("Hello, " + self.username + "!")

bbakjoo = User('Ju-Un', 'Park', 'bbakjoo', 33, 'pju2000@gmail.com')
bbakjoo.describe_user()
bbakjoo.gree_uesr()


# Working with classes and instances

class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
my_new_car = Car('audi' , 'a4', 2016)
print(my_new_car.get_descriptive_name())

# Setting a default value for an attribute

class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
        
my_new_car = Car('audi' , 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an attribute's value directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute's value through a method
class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it ateempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
              
            
my_new_car = Car('audi' , 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(50)
my_new_car.read_odometer()

# Incrementing an Attribute's Value through a method
class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it ateempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
     
    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading."""
        self.odometer_reading += miles         
            
my_used_car = Car('subaru' , 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# 9-4
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attribute"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """describing the restaurant"""
        print(self.name.title() + " is the " + self.type.title() + " restaurant.")
        
    def open_restaurant(self):
        """prints a message indicating that the restaurant is open"""
        print(self.name.title() + " is now open!")
    
    def read_number_served(self):
        """Print number of customers that the restaurant has served"""
        print("This restaurant has served " + str(self.number_served) + " customers.")
        
    def set_number_served(self, number_served):
        """ Set the number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        """ increment the number of customers who've been served."""
        self.number_served += increment        


first_restaurant = Restaurant('Than Brothers', 'vietnamese')

first_restaurant.read_number_served()

first_restaurant.set_number_served(20)
first_restaurant.read_number_served()

first_restaurant.increment_number_served(10)
first_restaurant.read_number_served()

# 9-5

class User():
    
    def __init__(self, first, last, username, age, email):
        self.first_name = first
        self.last_name = last
        self.username = username
        self.age = age
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("Age: " + str(self.age))
        print("Email Address: " + self.email)
        print("Number of login attemps: " + str(self.login_attempts))
        
    def greet_uesr(self):
        print("Hello, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        

bbakjoo = User('Ju-Un', 'Park', 'bbakjoo', 33, 'pju2000@gmail.com')
bbakjoo.describe_user()

bbakjoo.increment_login_attempts()
bbakjoo.describe_user()

bbakjoo.reset_login_attempts()
bbakjoo.describe_user()


# Inheritance
    # The __init__() Method for a child class

class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it ateempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
     
    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading."""
        self.odometer_reading += miles      
    

        
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

    # Defining Attributes and Methods for the child class
    
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

    # Override Methods from the parent class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def fill_gas_tank(self):
        """electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
my_tesla.fill_gas_tank()

    # Instances as Attributes
class Battery():
    """ A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message) 
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()    
my_tesla.battery.get_range()


# 9-6
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type attribute"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """describing the restaurant"""
        print(self.name.title() + " is the " + self.type.title() + " restaurant.")
        
    def open_restaurant(self):
        """prints a message indicating that the restaurant is open"""
        print(self.name.title() + " is now open!")
    
    def read_number_served(self):
        """Print number of customers that the restaurant has served"""
        print("This restaurant has served " + str(self.number_served) + " customers.")
        
    def set_number_served(self, number_served):
        """ Set the number of customers that have been served."""
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        """ increment the number of customers who've been served."""
        self.number_served += increment    
        
        
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def show_flavor(self):
        print("Following flavors are available:")
        for flavor in self.flavors:
            print("- " + flavor.title())
            
big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavor()


# 9-7
class User():
    
    def __init__(self, first, last, username, age, email):
        self.first_name = first
        self.last_name = last
        self.username = username
        self.age = age
        self.email = email
        
    def describe_user(self):
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("Age: " + str(self.age))
        print("Email Address: " + self.email)
        
    def greet_user(self):
        print("Hello, " + self.username + "!")
        
class Admin(User):
    
    def __init__(self, first, last, username, age, email):
        super().__init__(first, last, username, age, email)
        self.privileges = []
        
    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)
                
juun = Admin('Ju-Un', 'Park', 'bbakjoo', 32, 'bbakjoo@gmail.com')
juun.describe_user()

juun.privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
        ]

juun.show_privileges()


# 9-8
class User():
    
    def __init__(self, first, last, username, age, email):
        self.first_name = first
        self.last_name = last
        self.username = username
        self.age = age
        self.email = email
        
    def describe_user(self):
        print("Name: " + self.first_name.title() + " " + self.last_name.title())
        print("Username: " + self.username)
        print("Age: " + str(self.age))
        print("Email Address: " + self.email)
        
    def greet_user(self):
        print("Hello, " + self.username + "!")
        
class Privileges():
    
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        print("Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")

class Admin(User):
    
    def __init__(self, first, last, username, age, email):
        super().__init__(first, last, username, age, email)
        self.privileges = Privileges()

juun = Admin('Ju-Un', 'Park', 'bbakjoo', 32, 'bbakjoo@gmail.com')
juun.describe_user()

juun.privileges.show_privileges()

juun_privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
        ]

juun.privileges.privileges = juun_privileges
juun.privileges.show_privileges()


# 9-9
class Car():
    """ A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formateed descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it ateempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
     
    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading."""
        self.odometer_reading += miles      
        
class Battery():
    """ A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message) 
        
    def upgrade_battery(self):
        """Check the battery size and set the capacity to 85."""
        if self.battery_size < 85:
            print("Upgrading battery size in progress.")
            self.battery_size = 85
        else:
            print("Battery size is already at max.")
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()    
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
