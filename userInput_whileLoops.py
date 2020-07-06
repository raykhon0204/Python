#input() finction
#writing clear prompts
#each time you see the input() function, you should include a clear, 
#easy to follow prompt that tells the user exactly what king of info you're looking for
name = input("Please enter your name: ")
print("Hello, " + name + "!")

#you can store your prompt in a variable
prompt = "If you tell us who you are, we can personalize the message for you see."
prompt+="\nWhat is your first name?"
name = input(prompt)
print("\nHello, " + name + "!")

#using int() to convert string into integers
height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#try it yourself
#rental car
typeOfCar = input("What type of car you're looking for?")
print("Let me see if I can find " + typeOfCar)

#Restaurant Seating
numberOfPeople = input("How many people are their in your dining group?")
numberOfPeople = int(numberOfPeople)
if numberOfPeople >8:
    print("Sorry, you are going to have to wait for a table.")
else:
    print("Your table is ready!")

#while loop
current_number = 1
while current_number <=5:
    print(current_number)
    current_number+=1
#letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)