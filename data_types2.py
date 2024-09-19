# Boolean data types

print(type(True))

print(True)

print(type(False))

print(False)

a = 1000

b = 1000

print(a == b)

print(a is b)

print(a is not b)

# using boolean operators

print(True and True)

print(True and False)

print(False and True)

print(False and False)

print(True or True)

print(True or False)

print(False or True)

print(False or False)

print(not True)

print(not False)

# Set data types in python programming

print(type({1, 2, 3}))

print({1, 2, 3})

# adding elements to a set  

my_set = {1, 2, 3}

my_set.add(4)

print(my_set)

# removing elements from a set

my_set.remove(3)

print(my_set)

# checking if an element exists in a set

print(1 in my_set)

print(4 in my_set)

# Set operations

set1 = {1, 2, 3}

set2 = {3, 4, 5}

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.symmetric_difference(set2))


# Dictionary data types in python programming 

print(type({"name": "Sushanth", "age": 20}))

print({"name": "Sushanth", "age": 20})

# adding elements to a dictionary

my_dict = {"name": "Sushanth", "age": 20}

my_dict["city"] = "Bangalore"

print(my_dict)

# removing elements from a dictionary

del my_dict["age"]

print(my_dict)

# accessing elements in a dictionary

print(my_dict["name"])

print(my_dict.get("city"))

# checking if an element exists in a dictionary

print("name" in my_dict)

print("email" in my_dict)

# Dictionary operations

dict1 = {"name": "Sushanth", "age": 20}

dict2 = {"city": "Bangalore", "email": "sushanth@gmail.com"}

print(dict1.update(dict2))

print(dict1)

print(dict1.keys())

print(dict1.values())

print(dict1.items())

# nested dictionaries

nested_dict = {
    "name": "Sushanth",
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "Bangalore",
        "state": "Karnataka"
    }
}

print(nested_dict["address"]["city"])

# nested sets

nested_set = {
    "name": "Sushanth",
    "age": 20,
    "hobbies": {"reading", "painting", "cooking"}
}

print(nested_set["hobbies"])

# nested tuples

nested_tuple = {
    "name": "Sushanth",
    "age": 20,
    "friends": ("Charan", "Raghu", "Venkatesh")
}

print(nested_tuple["friends"][1])

# nested lists

nested_list = {
    "name": "Sushanth",
    "age": 20,
    "friends": ["Charan", "Raghu", "Venkatesh"]
}

print(nested_list["friends"][1])








