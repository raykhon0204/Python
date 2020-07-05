#store information about a pizza being ordered
pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese']}

#summarize the order
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)

#nesting list inside a dictionary
favorite_lang = {'jen': ['python', 'ruby'],
                 'sarah': ['C'],
                 'edward': ['ruby', 'go'],
                 'phil': ['python', 'haskell']}

for name, languages in favorite_lang.items():
    print("\n" + name.title()+ "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

#dictionary inside a dictionary
users = {'aeinstein': {
         'first': 'albert',
         'last': 'einstein',
         'location': 'princeton',
        },
         'mcurie': {
          'first': 'marie',
          'last': 'curie',
          'location': 'paris',
         } ,
         }
for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first']+ " "+user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

#try it yourself
#people
user_0 = {    
    'username': 'efermi',    
    'first': 'enrico',   
     'last': 'fermi',    }

user_1 = {
     'username': 'raya',
     'first': 'raykhon',
     'last': 'juraeva',
}

user_2 = {
     'username': 'esma',
     'first': 'esmira',
     'last': 'juraeva',
}

people = [user_1, user_2, user_0]
for user in people:
    print("This is the information about users: " +user['username'] + ", "+ 
    user['first']+ ", " +user['last'])
   
#pets
oreo = {'type': 'dog', 'ownerName': 'Esmira'}
kitty = {'type': 'cat', 'ownerName': 'Parisa'}
minnie = {'type': 'mouse', 'ownerName': 'Murod'}
pets = [oreo, kitty, minnie]
for pet in pets:
    print("This pet is a " + pet['type'] + ", the owner is " + pet['ownerName']+".")