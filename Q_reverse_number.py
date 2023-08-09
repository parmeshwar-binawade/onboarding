# Write a program for reverse a number

# method 1
num=2354
temp = 0
while num!=0:
    temp = temp*10 + num%10
    num = (num//10)
print("reverse number : %d" %temp)

# method 2
num=2354
print(str(num)[::-1])

# method 3
def number_reverse(num,temp=0):
    temp=temp*10+num%10
    num=num//10
    if num>0:
        temp=number_reverse(num,temp)
    return temp

num=2354
print(number_reverse(num))
