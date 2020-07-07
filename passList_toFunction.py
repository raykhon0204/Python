def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#modifying a list in a function
#unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
#completed = []

#simulate printing each design until none are left
#move each design to completed after printing
#while unprinted:
 #   current = unprinted.pop()
  #  print("Printing model: " + current)
   # completed.append(current)
#print("\nThe following models have been printed: ")
#for completed_model in completed:
 #   print(completed_model)

def print_models(unprinted, completed):
    while unprinted:
        current = unprinted.pop()
        print("Printing model: " + current)
        completed.append(current)
def show_completed(completed):
    print("\nThe following models have been printed: ")
    for completed_model in completed:
        print(completed_model)
unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted[:], completed)
show_completed(completed)

#preventing a function from modifying a list
#function_name(list_name[:]) the slice notation makes a copy of the list to send
#to the function

#try yourself
#magicians

def show_magician(name):
    
    for magician in magician_names:
        print("This is " + magician)




#Great magicians
def make_great(names):
    for magician in magician_names:
        print(f"the Great " + magician)

magician_names = ['tony', 'john', 'alice', 'elsa']
show_magician(magician_names)
make_great(magician_names)