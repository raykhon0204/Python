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