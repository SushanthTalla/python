# numerical data types program

marks = 100
price = 130.45
problem = 10 + 3j


print(type(marks))  
print(type(price))
print(type(problem))

# sequence data types program with strings

name = "Sushanth Talla"

print(type(name))

friends = ''' charan
              raghu
              venkatesh'''

print(type(friends))

# knowing length of string

schoolname = "vidhya Bharathi High School"

print(len(schoolname))

print(type(schoolname))

# indexing string

fruit = "Banana"

print(fruit)

print(fruit[0])

print(fruit[5])

print(fruit[-1])

# slicing string

program = "Data science using python"

print(type(program))

print(program)

print(program[0:10])

print(program[ :12])

print(program[12:])

print(program[2:4:1])

print(program[::-1])

# Deleting and updating a string 

string = "Hello World"

print(string)

del string

# concatenation using strings in python

first_name = "Sushanth"
last_name = "Talla"

full_name = first_name + " " + last_name

print(full_name)

# formatting strings in python

name = "Sushanth"
age = 20

print("My name is {} and I am {} years old.".format(name, age)) 

# Repeted strings 

print("Hello" * 5)

# string membership test

string = "Hello World"

print("World" in string)

print("World" not in string)

# string methods

string = "Hello World"

print(string.upper())

print(string.lower())

# lists in sequential data types

numbers = [1, 2, 3, 4, 5]

print(type(numbers))

print(numbers)

fruits = ["Banana","Apple","Mango"]

print(type(fruits))

print(fruits)

# accessing elements in a list

numbers = [1, 2, 3, 4, 5]

print(type(numbers))

print(numbers)

print(numbers[0])

print(numbers[2])

print(numbers[-1])

# changing list items

numbers = [1, 2, 3, 4, 5]

numbers[0] = 10

print(numbers)

# Add item and items to the list

numbers = [1, 2, 3, 4, 5]

numbers.append(6)

print(numbers)

numbers.extend([7, 8, 9])

print(numbers)

# adding a element at specified index

numbers = [1, 2, 3, 4, 5]

numbers.insert(2, 6)

print(numbers)

# deleting and removing list elements

numbers = [1, 2, 3, 4, 5]

numbers.remove(3)

friends = ["venky","raghu","shiva","sai"]

friends.pop(3)

print(friends)

print(numbers)

numbers.pop(2)

print(numbers)

numbers.clear()

print(numbers)

numbers = [10,20,30,40,50]

del numbers[1]

print(numbers)

# tuple in sequency data types

coordinates = (10, 20)

print(type(coordinates))

print(coordinates)

# accessing elements in a tuple

marks = (20,30,40,50)

print(type(marks))

print(marks[0])



















