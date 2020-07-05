#tuple is an immutable list, you can not change or modify the list
#looping through all values in a tuple
dimensions = (200, 50)
for dim in dimensions:
    print(dim)

#writing over a tuple
#you can assign a new value to a variable that holds a tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dim in dimensions:
    print(dim)

dimensions = (400, 200)
print("\nModified dimensions: ")
for dim in dimensions:
    print(dim)

foods = ("chicken", "fish", "soup", "osh", "mantu")
print("This is original menu:")
for food in foods:
    print(food)

foods = ("shurbo", "pelmeni", "fish", "soup", "osh", "mantu")
print("This is a new menu:")
for food in foods:
    print(food)



