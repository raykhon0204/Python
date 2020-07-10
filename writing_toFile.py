#writing to an empty file
#the second argument in open tell python that we want to open the file in write mode
#read mode ('r'), write mode ('w'), append mode ('a')
# read and write to the file ('r+')
#If you omit the mode argument, Python opens the file in read-only mode by default
#be careful opening a file in write mode ('w') because if the file does exist, 
# Python will erase the file before returning the file object.
fileName = 'programming.txt'
#with open(fileName, 'w') as file_obj:
    #file_obj.write("I love programming.")

with open(fileName, 'a') as file_obj1:
    file_obj1.write("I also love finding meaning in large datasets. \n")
    file_obj1.write("I love creating apps that can run in a browser. \n") 

prompt = "What is you name?\n"
prompt += "If there no more guests, please enter 'q' to quit.\n"
guest = ''
while guest != 'q':
    guest = input(prompt)
    with open('guests.txt', 'a') as guest_file:
        guest_file.write(guest + "\n")
        print("Hello, " + guest + ", welcome to the party!")

poll_active = True
while poll_active:
    response = input("Why do you like programming?\n")
    repeat = input("Would you like to let another person respond? (yes / no) ")
    with open('devs.txt', 'a') as dev_file:
        dev_file.write(response + '\n')
    if repeat == 'no':
        poll_active = False