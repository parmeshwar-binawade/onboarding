s="hello world, my name is parmeshwar"
print("Alternate character from string:  " + s[0:len(s):2])
print("Reverse String:  " + s[::-1])
print("Reverse Alternate character from string: " + s[len(s):0:-2])

print("Convert String into list: " + str(list(s)))
print("Split String into list: " + str(s.split(" ")))
print("replace space to '-': ",s.replace(" ", "-"))
print("replace convert to uppercase: ", s.upper())
print("String convert into capitalize: ",s.capitalize())
print("String swapcase: ",s.swapcase())
