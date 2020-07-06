#moving from one list to another

#start with users that need to be verified,
#and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users
#move each verified user into the list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verified user: " + current_user.title())
    confirmed_users.append(current_user)
#display all confirmed users
print("\nThe following users have been confirmed:")
for con_user in confirmed_users:
    print(con_user.title())

#removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

#filling a dictionary with User Input
responses = {}
#set a flag to indicate that polling is active
polling_active = True
while polling_active:
    #prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #store the response in the dictionary:
    responses[name] = response

    #find out if anyoune else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False
    
    #polling is complete, show the results
    print("\n---- Poll Results ----")
    for name, response in responses.items():
        print(name + "would you like to clime " +  response + ".")
    
    #try it yourself
    #Deli
    sandwitch_orders = ['veggie', 'turkey', 'salmon', 'tuna']
    finished_sandwitches = []
    while sandwitch_orders:
        sandwitch = sandwitch_orders.pop()
        print("I made your " + sandwitch.title())
        finished_sandwitches.append(sandwitch)
    print("\nThe following sandwitches have been made today:")
    for sand in finished_sandwitches:
        print(sand.title())
   
    #NO Pastarami
    sandwitch_orders = ['veggie', 'turkey', 'salmon', 'tuna']
    sandwitch_orders.append('pastarami')
    sandwitch_orders.append('pastarami')
    sandwitch_orders.append('pastarami')
    print("Sorry, we ran out of pastarami...")
    while 'pastarami' in sandwitch_orders:
        sandwitch_orders.pop()
    
    print(sandwitch_orders)

    #Dream vacation
    places = {}
    active_poll = True
    while active_poll:
        name = input("\nWhat is your name? ")
        place = input("\nIf you could visit one place in the world, where would you go?")

        places[name] = place

        repeat = input("\nWho else wants to the poll? (Answer y/n)")
        if repeat == 'n':
            active_poll = False
        print("This is the Poll Results: ")
        for name, place in places.items():
            print(name + " would like to go to " + place + ".")




    