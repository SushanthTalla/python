# A program to check some numbers are even or odd using functions and without functions
# without functions

from functools import reduce


number1 = 19
number2 = 18
number3 = 22

if(number1 % 2 == 0):
    print(number1, "is an even number")

else :
    print(number1, "is an odd number")

if(number2 % 2 == 0):
    print(number2, "is an even number")

else :
    print(number2, "is an odd number")

if(number3 % 2 == 0):
    print(number3, "is an even number")

else :
    print(number3, "is an odd number")

    
    # with functions

def evenorodd(number):
    if(number % 2 == 0):
        return number, "is an even number"
    else :
        return number, "is an odd number"
    
evenorodd(19)
evenorodd(18)
evenorodd(22)


# Returning functions 

def cubofnumber(number) :
    return number ** 3

print(cubofnumber(3))


# Anonymous functions

cubefun = lambda x: x ** 3
print(cubefun(3))


# Global and local variables

x = 10
def change_variable():
    global x
    x += 10
    print("Inside function:", x)

change_variable()    

print("Outside function:", x)


# Keyword Arguments

def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=25, name="John")

# Default arguments

def greet(name, age=30):
    print(f"Hello, {name}. You are {age} years old.")

greet("charan")

# Variable length arguments

def greet(*names):
    for name in names:
        print(f"Hello, {name}.")

greet("charan", "Raghu", "Venkatesh")

# Yield generators

def cube(numbers):
    for number in numbers:
        yield number ** 3

cubes = cube([1, 2, 3, 4, 5])

for cube in cubes:

    print(cube)

# filter,map,reduce 

numbers = [1, 2, 3, 4, 5]

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(filtered_numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)

squared_numbers_sum = sum(squared_numbers)

print(squared_numbers_sum)

def addAll(a,b) :
   
    return a + b

numbers = [20,2,3,10,5]

result = reduce(addAll,numbers,18)

print(result)

# lets convert to lambda

numbers =  [20,2,3,10,5]

result = reduce(lambda a, b: a + b, numbers, 18)

print(result)



























