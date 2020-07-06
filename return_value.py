#the return statement takes the value from inside the function and sends it back
#to the line that called the function
def get_formatted_name(first, last):
    full_name = first + ' '+ last
    return full_name.title()
musician = get_formatted_name('jimmi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name1(first_name, last_name, middle_name=''): 
    if middle_name:        
        full_name = first_name + ' ' + middle_name + ' ' + last_name     
    else:        
        full_name = first_name + ' ' + last_name    
    return full_name.title()
musician1 = get_formatted_name1('jimi', 'hendrix') 
print(musician1)
musician1 = get_formatted_name1('john', 'hooker', 'lee') 
print(musician1)

#returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

artist = build_person('esmira', 'juraeva')
print(artist)

#using function with while loop
def get_name(first_name, last_name):
    fullName = first_name + " " + last_name
    return fullName
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    name1 = get_name(f_name, l_name)
    print("\nHello, "+ name1 + "!")