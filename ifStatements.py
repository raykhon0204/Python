#to make the value case insensitive use lower()
car = 'Audi'
print(car.lower()=="audi")

#checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#numerical comparison
age = 17
print(age == 18)

answer = 18
if answer!=42:
    print("That is not the correct answer. Please try again!")

#checking multiple conditions
a1 = 22
a2 = 18
if a1>21 or a2 > 21:
    print("You guys can come to the bar!")
else:
    print("Sorry, you need to grow up!")
    
#checking whether a value is in a list
#use a keyword in
toppings= ['mushroom', 'onions', 'pineapple']
print('mushroom' in toppings)

#check if the value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

#boolean expression
fruit = 'apple'
print("Is fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

city = 'Paris'
print(city == 'paris')
print(city.lower() == 'paris')
print("__________________________________________")

fruits = ['apple', 'banana', 'grapes', 'melon']
print('melon' in fruits)
print('watermelon' not in fruits)
