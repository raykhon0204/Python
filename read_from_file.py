#read the file
#with open('pi_digits.txt') as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())

#file paths
#file_path = 'Python/pi_digits.txt on Windows - \
#with open(file_path) as file_object:
#reading line by line
with open('stylingCode.txt') as newFile:
    for line in newFile:
        print(line.rstrip())
    
#making a list of lines from a file
fileName = 'pi_digits.txt'
with open(fileName) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#working with a file's contents
with open('file.txt') as file_object1:
    lines = file_object1.readlines()

file_string = ''
for line in lines:
    file_string += line.rstrip()

print(file_string)
print(len(file_string))

#large files: One Million Digits
with open('pi_million_digits.txt') as f_object:
    lines = f_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))

#Is your Birthday Contained in PI?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

#try it yourself
#Learning Python
with open('learnin_python.txt') as file_object2:
    for line in file_object2:
        print(line.rstrip())
    
    lines = file_object2.readlines()
    for line in lines:
        print(line.rstrip())
    
    