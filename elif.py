age = 12
if age < 4:
    price = 0
elif age > 18:
    price = 5
else:
    price = 10
print(f"Your admission cost ${price}")

requested_topp = ['mushroom', 'green peppers', 'extra cheese']
for req_top in requested_topp:
    print("Adding " + req_top + ".")
print("\nFinished making pizza!")

#when the name of list is used in an if stat. Python returns True
#if the list contains at least one item; an empty list evaluates to False

#using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topp in requested_toppings:
    if requested_topp in available_toppings:
        print("Adding "+ requested_topp + ".")
    else:
        print("Sorry, we don't have " +requested_topp + ".")
print("\nFinished making your pizza!")

userName = ['admin', 'pari', 'esma', 'muko', 'raykhon']
for user in userName:
    if user =='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " +user+", thank you for logging in again." )
print("_____________________________________________________________") 
#checking if the list is empty
users = []
if user not in users:
    print("We need to find some users!")
print("______________________________________________________________")

websiteUsers = ['admin', 'pari', 'user3', 'muko', 'raykhon']
newUsers = ['user1', 'user2', 'user3', 'user4', 'user5']

for user in newUsers:
    if user.lower() in websiteUsers:
        print("The username is not available, please enter new usernanme.")
    else:
        print("The username is available.")

print("_______________________________________________________________")

ordinalNumbers = [1,2,3,4,5,6,7,8,9]
for number in ordinalNumbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")