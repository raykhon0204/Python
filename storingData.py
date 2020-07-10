import json

#dump() function takes two arguments: a piece of data to store and a file obj it 
#can use to store the data
numbers = [2, 4, 5, 6, 7, 8]
filename = 'numbers.json'
with open(filename, 'w') as jf_object:
    json.dump(numbers, jf_object)

#load() reads the file back
with open(filename) as jf_object:
  numbers = json.load(jf_object)
print(numbers)

#saving and reading user-generated data
""" username = input("What is your name? ")
filename1 = 'username.json'
with open(filename1, 'w') as user_file:
    json.dump(username, user_file)
    print("We'll remember you when you come back, " + username.title() + "!") """
def greet_user():
    filename1 = 'username_new.json'
    try:
        with open(filename1) as user_file:
            username = json.load(user_file)
    except FileNotFoundError:
            username = input("What is your name? ")
            with open(filename1, 'w') as user_file:
                json.dump(username, user_file)
                print("We'll remember you when you come back, " + username.title()+ "!")
    else:
        print("Welcome back, " + username.title() + "!")

#refactoring
greet_user()
