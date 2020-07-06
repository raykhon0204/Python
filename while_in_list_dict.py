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