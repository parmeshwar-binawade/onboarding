"""
# 1. Write lambdas to:
    # a. Square a number x2
    # b. Inverse a number 1/x
    # c. Negate a number

n=4
num1=lambda n:n*n
num2=lambda n:1/n
num3=lambda n:n-(n+n)

print("Square a number {} is: {}".format(n,num1(n)))
print("Inverse a number {} is: {}".format(n,num2(n)))
print("Negative Number of {} is: {}".format(n,num3(n)))



# 2. Use reduce function and an appropriate lambda to find the maximum number in a list.
from functools import reduce
list1=[3,6,3,5,8,7,0]
print(reduce(lambda x,y: x if x > y else y,list1))


# 3. Write a function map_multiple that takes a list of functions/lambdas as first argument and a
# sequence type as second argument.
# The function picks first lambda from list, applies it to first element, then applies the second
# function to the result of first one and ….
# Similarly it does for each element and generates a mapping of input to output

# def map_multiple(functs, sequence):
#  # write definition here
# Ex: let list of lambdas be from question 1 and the list on numbers be [1,2,4]

def square_number(n):
    return n*n

def inverse_number(n):
    return 1/n

def negative_number(n):
    return (n-(n+n))

num=[1,2,4]
result=map(square_number,num)
print("Square number is {}" .format(list(result)))

result=map(inverse_number,num)
print("Inverse number is {}" .format(list(result)))

result=map(negative_number,num)
print("negative number is {}" .format(list(result)))



# 4. Predict the output of following code:

from functools import reduce
f=lambda x,y: x if x >y else y
l=[10,30,50,30,10]
num=reduce(f,l)
print(num)
# output 50

# 5. Find output of following:
functs=[lambda x:x**0.5, lambda x:1/x]
l=[1,4,16,64]
ans=[]
for num in l:
    res=num
    for funct in functs:
        res=funct(res)
    ans.append(res)
print(ans)

# output [1.0, 0.5, 0.25, 0.125]



# 6. Use filter function to filter a list of numbers and strings such that the result contains only
# numbers. (Hint : Use isinstance method)

def verify(o):
    return isinstance(o,int)
l=[2,4,'s',6,'t']
result=filter(verify,l)
print(list(result))


# foot 3.281=1 meter
# 1 inch=0.0254
# 1 foot=0.3048 meter

# 7. Assume a list containing heights ft and inches in the form of a list of string
# Example : l = [‘5ft10in’, ‘5ft’, ….]
# Write a function to convert the heights to meter. Use map function along with your function to
# convert everything to m.
import re
l = ['5ft10in', '5ft', '3ft9in']
m=[]
def ft_to_meter(l):
        h = re.findall(r'\d+', l)
        if len(h)==1:
            return(int(h[0])*0.3048)
        else:
            return(int(h[0])*0.3048+int(h[1])*0.0254)


m=m + (list(map(ft_to_meter,l)))
print(m)

"""

# 8. Write the implementation for the map function yourself by the name my_map()

l=[1,2,3]

def my_map(a):
    return a**2
print(list(map(my_map,l)))