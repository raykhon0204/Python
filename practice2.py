for number in range(1, 21):
    print(number)

oneMil = list(range(1, 1000000))
print(min(oneMil))
print(max(oneMil))


oddNum = list(range(1, 22, 2))
print(oddNum)

three = []
for value in range(3, 31):
    three.append(value*3)
print(three)

#this is using a list comprehension
cubes = [value**3 for value in range(1,11)]
print(cubes)

# in Python3, dividing two ints results in a float, but using // acts as integer division.

# Python3
#>>> 10 / 3
#3.3333333333333335
#>>> 10 // 3
#3
#To remove the space we can use  sep=""

print(*range(0,4), sep="")

print(*(2,3),sep=",")

print(*[0,5,7], sep="\n")