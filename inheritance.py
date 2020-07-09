#when one class inherits from another it automatically takes on all the attributes and 
#methods of the first class
from classes import Car
from battery import Battery
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #defining attribute and methods for the child class
        #initializing attribute specific to an elec. car
        self.battery_size = Battery()
    
   

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_description())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()

#Instances as attributees
#when the class has a lot of attributes and methods you can move them to 
#separate class like Battery and use Battery instance as an attribute in the 
#ElectricCar class
