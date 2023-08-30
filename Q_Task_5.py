'''
# 1. WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
# BMI.
# Write code that calls this function after taking height and weight as inputs and then prints
# underweight, normal, overweight or obese depending on the value of BMI.
# Refer this link for the ranges:
# https://en.wikipedia.org/wiki/Body_mass_index


def bmi(h,w):
    return w/(h/100)**2
h=int(input('Enter a height in cm: '))
w=int(input('Enter a weight in kg: '))
bmi_value=bmi(h,w)
print(bmi_value)
if bmi_value < 18.5:
    print("You are Underweight")
elif bmi_value < 25:
    print("You are in normal range")
elif bmi_value < 30:
    print("You are in overweight")
else:
    print("you are in obese")


# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

a=int(input('Enter a age'))
b=int(input('Enter a age'))
c=int(input('Enter a age'))
old=young=0
if a>b and a>c:
    print("{} is oldest age".format(a))
    if b > c:
        print("{} is youngest age".format(c))
    else:
        print("{} is youngest age".format(b))
elif b>c and b>a:
    print("{} is oldest age".format(b))
    if a > c:
        print("{} is youngest age".format(c))
    else:
        print("{} is youngest age".format(a))
else:
    print("{} is oldest age".format(c))
    if a > b:
        print("{} is youngest age".format(b))
    else:
        print("{} is youngest age".format(a))

# 3. WAP to input a number and check if number is divisible by both 5 and 7.
num=int(input("Enter a number: "))
if num % 5 ==0 and num % 7 ==0:
    print("{} number is divisible by 5 and 7".format(num))
else:
    print("{} number is not divisible by 5 and 7".format(num))


# 4. WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
# in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
# functions)
def is_alphabet(s):
    for i in s:
        if ord(i)<65 or ord(i)>90 and ord(i)<97 or ord(i)>122:
            return False
    return True
s=input("Enter a string: ")
status=is_alphabet(s)
if status==True:
    print("All character are alpahbets")
else:
    print("All character are not alpahbets")


# 5. WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise
# false.
def CheckLeapyear(Year):
    if((Year % 400 == 0) or  (Year % 100 != 0) and (Year % 4 == 0)):
        print("Given Year is a leap Year");
    else:
        print ("Given Year is not a leap Year")

Year = int(input("Enter the number: "))
CheckLeapyear(Year)


# 6. WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
# as arguments and returns the number of days in the month.
# Use the function is_leap_year() to check the special case of 29 days in leap year for month of
# FEB. [Use dictionary to store the mapping of month and days.]
import calendar
li=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month_name=input("Enter three character of month: ")
year=int(input("Enter year in (YYYY) format: "))
print(calendar.monthrange(year, li.index(month_name.title()))[1])



# 7. Update the above program to work with both 3 character month and complete name of month.
import calendar
li=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
month_name=input("Enter three character of month: ")
year=int(input("Enter year in (YYYY) format: "))
print(calendar.monthrange(year, li.index(month_name.title()[slice(3)]))[1])

'''


# 8. WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
# common words in both the sentences.
# [Hint: store all the in a set. Read the documentation for set.]

def uncommon_words(s1,s2):
    return s1.intersection(s2)
s1=input("Enter string1: ")
s2=input("Enter string2: ")
s1_set=set(s1)
s2_set=set(s2)
print(uncommon_words(s1_set,s2_set))
