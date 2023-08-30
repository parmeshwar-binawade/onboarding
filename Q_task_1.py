"""
# 1. Predict Output,
S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2))

# output is: 5 14

# 2. WAP to input a string and print its length.
s=input("Enter a string: ")
print(len(s))

# output is: Enter a string: parmeshwar
# 11

# 3. WAP to input 2 numbers and print their sum and difference.
n1=int(input("Enter number1"))
n2=int(input("Enter number2"))
print(n1+n2)
print(n1-n2)

# 4. Predict Output,
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)
# abde

# 5. Predict Output,
s1 = 'ab' *4
print(s1)
# abababab

# 6. WAP to input a string s and a number n. Print the string n times on the screen,
#    each should appear in a separate line (do not use any kind of loops, use the multiplication operator).

def display(s):
    print(s)

s=input("Please enter string")
n=int(input("Please enter number"))
map(display,s)

# 7. Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))
# output
# <class 'str'>
# 19

# 8. Find the name of function to find the square root. (see all the options available in dir() of builtins)
import math
print(dir(math.sqrt))

import math


# 9. WAP to input a number and print its square root ().
num=9
print(math.sqrt(num))

# 10. WAP to input 4 numbers from user and print their average
n1=int(input("Please enter number1: "))
n2=int(input("Please enter number2: "))
n3=int(input("Please enter number3: "))
n4=int(input("Please enter number4: "))

print((n1+n2+n3+n4)/4)


# 11. Use the help function to check what the abs function in python does.
try:
    help(abs)
    print("Abs function supported in python")
except:
    print("Abs function not supported in python")

"""

# 12. What is the output of this code when run from python interpreter.
print(__name__)
# output
# __main__