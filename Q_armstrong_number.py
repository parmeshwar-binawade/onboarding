# write a program to check armstrong number

# method 1
num=153
result=0
for i in str(num):
    result=result+int(i)*int(i)*int(i)

if result == num:
    print("Given Number is armstrong number")
else:
    print("Given number is not armstrong number")

# method 2
num=153
result=0
result=sum([result+int(i)*int(i)*int(i) for i in str(num)])
if result == num:
    print("Given Number is armstrong number")
else:
    print("Given number is not armstrong number")
