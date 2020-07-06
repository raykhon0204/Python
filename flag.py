#flag acts as signal to the program
#we can write our program so it can rum while the flag is set to True
#and stop running if any of several events sets the value of the flag to False
prompt = "\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter quit to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter quit when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " +city.title() + "!")

#using continue in a Loop
current_number = 0
while current_number < 10:
    current_number+=1
    if current_number % 2 == 0:
        continue
    print(current_number)

#adding infinite loops
#avoid writing x = 1 instead x+=1
