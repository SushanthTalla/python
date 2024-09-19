# if else statements using python

number = 7

if (number %2 == 0):
    print("The number is even ")

else :
    print("The number is odd ")

age = 18

if (age >= 18):

     print("You are eligible to vote ")

else:
     print("You are not eligible to vote ")

# Nested if program in python

number = int(input("Enter a number"))

if (number %2 == 0):
     
     if (number % 4 == 0):
          
          print("The number is divisible by 2 and 4")

     else :

         print("The number not divisible by 2 and 4")

else :

       print("The number is not divisible by 2 and 4")


# if- elif program in python
# program for btech college admissions according to their Ranks


Rank = int(input("Enter your Rank"))

if (Rank <= 1000):

    print("congrats ,You are eligible for admission in college 1")

elif (Rank > 1000 and Rank < 10000):
     
     print("congrats ,You are eligible for admission in college 2")

elif (Rank > 1000 and Rank <= 40000):

     print("congrats ,You are eligible for admission in college 3")

else :

     print("sorry ,You are not eligible for admission in any college")


# shorthand if- elif program in python

Rank = int(input("Enter your Rank"))

print("Congratulations, You are eligible for admission in college " + ("1" if Rank <= 1000 else ("2" if Rank > 1000 and Rank < 10000 else "3")))


# itarative loops with for loops 

i = 0

for i in range(10):

    print(i)

# Using start,stop,step in Range     

for i in range(4,46,3):

    print(i)

# using some mathematical functions

NumberList = [1,2,3,10,15,19,24,12]  

for number in NumberList:

    print(number)

    print(number * 5)

    print(number ** 2)

    print(number % 2 == 0)

    print(number / 2)

# using some strings in for loop

name = "Ramcharan"

for char in name:

    print(char)


# finding vowels in strings using for loop

name = input("Enter your name")

vowels = "aeiouAEIOU"

for char in name:

    if char in vowels:

        print(char,"it is vowel")

    else :

        print(char,"it is not vowel")

# using control statements using break,continue,pass
# program for break statement

name = input("enter your name")

vowellist =  "aeiouAEIOU"

for char in name:

    if char in vowellist:

        print(char,"it is vowel")

        break

# continue statement program

name = input("Enter your name")

vowellist =  "aeiouAEIOU"

for char in name:

    if char in vowellist:

        print(char,"it is vowel")

        continue

# while loop statements

i = 0

while i < 10:

    print(i) 


name = "sushanth" 

while name!= "Sushanth":

    print("Hello",name)
    
    name = input("Enter your name again")

    if name == "Sushanth":

        print("Congratulations, You have entered correct name")



    















     










     
     





