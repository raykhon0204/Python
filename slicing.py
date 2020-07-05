#this is caleed slicing, if you omit first index, python
#will start from the beginning of the list
players =['charles', 'martina', 'michael', 'florece', 'eli']
print(players[0:2])

#looping through a slice
pl = ['charles', 'martina', 'michael', 'florece', 'eli']
print("Here are the first three players on my team: ")
for pl1 in pl[:3]:
    print(pl1.title())

#copying the list
my_food = ['pizza', 'falafel', 'carrot cake']
f_food = my_food[:]
print("My favorite foods are: ")
print(my_food)
print("\nMy friend's favorite foods are: ")
print(f_food)

my_food.append('cannoli')
f_food.append("ice cream")

print(my_food)
print(f_food)