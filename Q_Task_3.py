'''
# 1. Predict Output,
S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2))

# 5 14



# 2. WAP to input a string and print its length.
s=input("Enter a string: ")
print(len(s))

# 3. WAP to input 2 numbers and print their sum and difference.
n1=int(input("Enter a number-1: "))
n2=int(input("Enter a number-2: "))
print("Addition is {}".format(n1+n2))
print("Substraction is {}".format(n1-n2))


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

s=input("Enter a String-1: ")
a=input("Enter a String-2: ")
n=int(input("Enter a number: "))
print(s*n)
print(a*n)



# 7. Predict Output,
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))
print(len(s3))
# after resolving missing ) paranthesis error
# <class 'str'>
# 19

# 8. Find the name of function to find the square root. (see all the options available in dir() of builtins)
# Python3 program to demonstrate the
# sqrt() method

import math

print(math.sqrt(8))

# 9. WAP to input a number and print its square root ().
import math

num=int(input("Enter a number"))
print(math.sqrt(num))


# 10. WAP to input 4 numbers from user and print their average

num1=int(input("Enter a number1: "))
num2=int(input("Enter a number2: "))
num3=int(input("Enter a number3: "))
num4=int(input("Enter a number4: "))
print((num1+num2+num3+num4)/4)


# 11. Use the help function to check what the abs function in python does.

print(help(abs(4)))
'''
# 12. What is the output of this code when run from python interpreter.
print(__name__)

#output: __main__
