pizzaTypes = ["cheese", "pepperoni", "veggie", "broccoli", "cesar"]
for pizza in pizzaTypes:
    print(f"I like " + pizza.title() +". "+ "And my kids love them too"+".\n")

pets = ["dog", "cat", "mouse", "lizard"]
for pet in pets:
    print(f"A " + pet+ " "+ "would make a great pet. But it is very expensive to have a pet in your home!")


#create a list with range()
even_numbers = list(range(2, 21, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,33,23,76,88,99,78,66,55,45,64,52,11,24,27,18,19]
print(min(digits))
print(max(digits))
print(sum(digits))