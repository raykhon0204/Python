#making an object from a cladd is called Instantiation, and you work with instances
#of a class

#creating the dog class
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
    #the init method is a special method, python runs automatically whenever we 
    #create a new instance based in the dog cladd
    #a function that's part of a class is a method
    #variables that are accessable through instances called attributes
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " yeats old.")

#calling methods
# after we create an instance from the class Dog we can use dot notation
# to call any method defined in Dog

my_dog.sit()
my_dog.roll_over()    

#creating multiple instances
your_dog = Dog('Lucy', 5)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " yeats old.")
your_dog.sit()

#try it yourself
#Restaurant
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print("This is restaurant " + self.name.title() + " and cuisine type is " + self.cuisine.title())
    
    def open_restaurant(self):
        print("The restaurant is now open to serve our customers!")

res1 = Restaurant('Afsona', 'uzbek')
res1.describe_restaurant()

res2 = Restaurant('Baku Palace', 'azerbayjan')
res2.describe_restaurant()

res3 = Restaurant('Anatoliy', 'turkish')
res3.describe_restaurant()

#woring with classes and instances
#the car class
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_description(self):
        long_name = str(self.year) + ' ' +self.make + ' ' + self.model
        return long_name.title()
    #setting a default value for an atribute
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
         if mileage >= self.odometer_reading:            
            self.odometer_reading = mileage        
         else:              
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car('Audi', 'a4', 2016)
print(my_car.get_description())
#my_car.read_odometer()

#modifying attribute values
# 1. modifying an attribute's value direbctly
#my_car.odometer_reading = 88
#my_car.read_odometer()
# 2. modifying through a method
   

my_car.update_odometer(99)
my_car.read_odometer()
my_car.increment_odometer(45)
my_car.read_odometer()
