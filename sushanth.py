# python Hello world program

print('Hello world')

# variables in python
name = 'charan'
age = 20

print(name)
print(age)

# arithmetic operations using python

a = 100
b = 200
c = a + b

print(c)

d = 120
e = 176

print(d+e)
print(d-e)
print(d*e)
print(d/e)
print(d//e)
print(d%e)

# Case Sensitive operations using python

sum = 143
Sum = 1456

print(sum)
print(Sum)

# String Concatenation and method operations using python 

a = "sus" + "ha" + "nth" + "talla"
print(a)

b = "chinnu" + "paleti"
print(b)

x = 'my'
y = 'personal'
z = x + y
print(z)

name = input("Enter your name:")
result = len(name)

print(result)

result = name.find("h")
print(result)

result = name.replace("s", "S")
print(result)

result = name.capitalize()
print(result)

result = name.lower()
print(result)

result = name.isdigit()
print(result)

result = name.isalpha()
print(result)

# Global variables and Local variables

sum = 10
def calculate ():
    currentsum = 200
    totalsum = currentsum + sum
    print(totalsum)

calculate();

print(sum)

# initialize local values in global variables

sum = 30
def calculate ():
    sum = 20
    currentsum = 230
    totalsum = currentsum + sum
    print(totalsum)

calculate() ;

print(sum)

# Changing the values of global variables in local space

sum = 60
def calculate ():
    global sum
    sum = sum + 20
    currentsum = 250
    totalsum = currentsum + sum
    print(totalsum)
calculate() ;

print(sum)

# user input and output funtions using python
# program to demonstrate input and output

cash = 1000
print("Take your cash",cash)

cash = 2000
Balence = 4000

print("Take your cash :",cash)
print("Your current balance is :", Balence)

# program with using sep = ' '

cash = 1000
RemainingAmount = 7500
print("Take your cash :", cash,"Your RemainingAmount :",RemainingAmount, sep='   ')

print("Thankyou")


print("Take your cash :", cash,"Your RemainingAmount :",RemainingAmount, sep='-------. ')

print("Thank you")


# program with using end = '\n'

cash = 1000
RemainingAmount = 7500
print("Take your cash :", cash, end=' ')
print("Your Remaining Amount :", RemainingAmount)

print("Thank you")






      













