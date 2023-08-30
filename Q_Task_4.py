
'''

# 1. Write a for loop to print numbers from 1 to 10. All numbers should be in separate lines.

for i in range(1,11):
    print(i)

# 2. Write a for loop to print numbers from 10 to 1. All numbers should be in separate lines.
for i in range(10,0,-1):
    print(i)

# 3. Print Elements at Odd indexes from a list (Using for loop)
l = [10,11,20, 21,30, 31, 40, 41]
for i in l:
    if i%2 != 0:
        print(i)

import random

# 4. Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
# a for loop.
li=[]
sum=0
avg=0
temp=0
for i in range(0,5):
    temp=random.randint(1,100)
    li.append(temp)
    sum=sum+temp
print(li)
print(sum)
print(sum/5)


# 5. WAP to input a string and print individual characters in the string using for loop.

s=input('Enter a String: ')
for i in s:
    print(i)

# 6. WAP to input a string and print the ASCII value of each character in the string.

s=input('Enter a String: ')
for i in s:
    print(i,end=" ")
    print(ord(i))

# 7. WAP to input a string and store ASCII values of all characters in a tuple.
s=input('Enter a String: ')
t=()
for i in s:
    t=t+(ord(i),)
print(t)

# 8. Write a function that takes a list of numbers from user as argument and returns the sum of only
# odd numbers (Use only for loop. No need to use if statement).

def my_sum2(numbers):
    print(sum([n * (n % 2 != 0) for n in numbers]))

def my_sum(numbers):
    s = 0
    for n in numbers:
        s += n * (n % 2 != 0)
    print(s)

def list_of_number():
    li=[]
    for i in range(5):
        num=input("Enter a number: ")
        li.append(num)
    return li

li=list_of_number()

my_sum2(li)
my_sum(li)

# 9. WAP to input a list of numbers and store in a tuple. Now input another number and print the
# index of this number in the tuple.

t=()
for i in range(5):
    temp=int(input("Enter a number: "))
    t=t+(temp,)
print(t)
num=int(input("Enter existing number from tuple"))
print(t.index(num))

# 10. WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
li = []
for i in range(10):
    num = input("Enter a number: ")
    li.append(int(num))
print(li)



# 11. Update the above program to also print the sum of numbers.
li = []
sum=0
for i in range(10):
    num = input("Enter a number: ")
    li.append(int(num))
    sum=sum+num
print(li)
print(sum)



# 12. WAP to input a number and print all numbers from 1 till that number
num=int(input('Enter a number: '))
if num > 1:
    for i in range(1,num+1):
        print(i)
else:
    print("Enter greater than 1 number")

'''

# 13. WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
#     whose factorial is to be found.
#         Ex: if n = 4 output should be 24
#         4! = 1x2x3x4 = 24

n=int(input('Enter a number: '))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
