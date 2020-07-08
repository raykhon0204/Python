#sometimes you won't know ahead of time how many arguments a function needs to accept
#python allows a function to collect an arbitrary number of arguments from the 
#calling statement

#the asterisk in the parameter name tells the python to make an empty tupple called
#toppings and pack whatever values it receives into the tupple
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#mixing positional and arbitrary arguments
#python matches positional and keyword arguments first and then collects any remaining
#arguments in the final parameter
def doing_pizza(size,*toppings):
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for top in toppings:
        print("- " + top)
doing_pizza(16, 'pepperoni')
doing_pizza(12, 'mushrooms', 'extra cheese')

#using arbitrary keyword argument
#double asterisks cause python to create an empty dictionary 
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

#try it yourself
#Sandwiches
def make_sandwitch(*ingredients):
    print("These are the ingredients you have selected for your sandwitch:")
    for ingredient in ingredients:
        
        print("- " + ingredient)

make_sandwitch('lettuce', 'tomatoes', 'onion', 'ketchup', 'pickles')

#User Profile
my_profile = build_profile('raykhon', 'juraeva', gender = 'female', occupation = 'QA Engineer', location = 'New Jersey')
print(my_profile)

#cars
def make_car(manufacture, module, **carInfo):
    car = {}
    car['car_manufacture'] = manufacture
    car['car_module'] = module
    for key, value in carInfo.items():
        car[key] = value
    return car

subaru = make_car('subaru', 'outback', color = 'blue', tow_package = 'True')
print(subaru)