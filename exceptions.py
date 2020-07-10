#python uses special objects called exceptions to manage errors
#that arise during a program's execution
#try-except block askd python to do something, but it also tells what to do if an
#exception is raised
#when you use try-except your program will continue running even if things 
#start to go wrong, instead of traceback, which can be confusing for users to read
#users will see friendly error messages that you write

#handling the zeroDivisionError Exception
""" try:
    print(5/0)
except ZeroDivisionError:
    [print("You can't divide by zero!")]

#using Exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    # The error occurs on the line that performs the division, so that’s 
    # where we’ll put the try-except block. This example also includes an else 
    # block. Any code that depends on the try block executing successfully goes 
    # in the else block:
    try:
        answer = int(first_number)/ int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer) """
    # Sometimes you’ll have additional code that should run only if the try block was successful; 
    # this code goes in the else block. 

    #Handling the FileNotFoundError Exception
file_name = 'alice.txt'
try:
    with open(file_name) as f_o:
        contents = f_o.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)

#analyzing text
#splir() method separates a string into parts wherever it finds a space and
#stores all the parts of the string in a list
else:
    #count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file "  + file_name + " has about " + str(num_words) + " words." )

#failing silently
#to make the program to fail silently , you write a try block as usual
#but you explicitly tell python to do nothing in the except block
#pass statement will tell python to do nothing in block

def count_words(file_name):
    try:
        with open(file_name) as f_o:
           contents = f_o.read()
    except FileNotFoundError:    
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "  + file_name + " has about " + str(num_words) + " words." )
filenames = ['alice.txt', 'programming.txt', 'guests.txt', 'devs.txt'] 
for filename in filenames:    
    count_words(filename)   

#try it yourself
#Addition
print("Give me two number and I'll add them.")
print("Enter q to quit the program!")
while True:
  first1 = input('\nFirst number: ')
  if first1 == 'q':
      break
  second2 = input("Second number: ")
  if second2 == 'q':
      break
  try:
     answer = int(first1) + int(second2)
  except ValueError:
     print("Please, enter a number, not a letter!")
  else:
     print(answer)