from name_function import get_name
print("Enter 'q' at any time to quit. ")
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    last = input("Please give me your last name: ")
    if last == 'q':
        break

    getName = get_name(first, last)
    print("\nNeatly formatted name: " + getName + '.')