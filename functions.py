def display_message():
    print("I am learning functions in this chapter.")

display_message()

def favorite_book(book):
    print("One of my favorite books is " + book)

favorite_book('Alice in Wonderland')

#positional arguments
#matching the arguments provided with the parameters in the function based on the order of the 
#argument provided
def describe_pet(type, name):
    print("\nI have a "+ type + ". ")
    print("My "+ type + "'s name is " +  name.title() + ".")

describe_pet('dog', 'oreo')
describe_pet('cat', 'kitty')

#keyword argument - is a name-value pair that passes to a function
def describe_pet1(animal_type, pet_name): 
    print("\nI have a " + animal_type + ".")    
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")    

describe_pet1(animal_type='hamster', pet_name='harry')

#default values
#you can define a default value for each parameter
def describe_pet2(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")    
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet2(pet_name='willie')

#try it youself
#T-shirt
def make_shirt(size ='L', message = 'I Love Python'):
    print("In this shirt size " +size+ ", the message " + message + " will be printed, thanks for ordering!")

make_shirt()
make_shirt('M', 'I Love Java')


