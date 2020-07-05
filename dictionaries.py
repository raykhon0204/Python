alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print("_______________________________________")

#modifying the value in a dictionary
alien1 = {'xpos': 0, 'ypos': 25, 'speed': 'medium'}
print("Original x position: " + str(alien1['xpos']))
#move the alien to the right.
#determine how far to move the alien based on its current speed.
if alien1['speed'] == 'slow':
    x_increment = 1
elif alien1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#this new position is the old position plus the increment.
alien1['xpos'] = alien1['xpos'] + x_increment
print("New x position: " + str(alien1['xpos']))

#deleting unwanted key-value pair using del

#del alien1['points']

#dictionary of similar objects
favorite_lang = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is " + favorite_lang['sarah'].title() + ".")

#try yourself
people = {'firstName': 'Parisa', 'lastName': 'Juraeva', 'age': 8, 'bornCity': 'Brooklyn',
          }
for key, value in people.items():
    print("\nKey: " + key)
    print(f"Value: {value}")
print("________________________________________________________")

#looping through all the keys in a dictionary
for name in favorite_lang.keys():
    print(name.title())
#lets find out if Erin took the poll
if 'erin' not in favorite_lang.keys():
    print("Erin, please take our poll!")
#looping through a dictionary's keys in order
for name in sorted(favorite_lang.keys()):
    print(name.title()+ ", thank you for taking the poll.")

for language in favorite_lang.values():
    print(language.title())

#to see each values chosen without repetition we can use set
#a set is similat to a list except that each item in the set must be unique
for language in set(favorite_lang.values()):
    print(language.title())

favorite_lang['parisa'] = 'java'
favorite_lang['esmira'] = 'C#'
favorite_lang['raykhon'] = 'SQL'
print(favorite_lang)
print("____________________________________________________")

#make an empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(0,15):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#to change the first three aliens to yellow, medium speed aliens worth 10 points

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

#show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")
#show how many aliens have been created
#print("Total number of aliens: " + str(len(aliens)))

