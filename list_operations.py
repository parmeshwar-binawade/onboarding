li1=['a','b','c','d','a']
li2=['A','B','C','D','a']

print("Merge two list: ", str(li1+li2))

li1.append(li2)
print("Append two list: " +str(li1))

li1.remove('a')
print("Remove specific character 'a': ", str(li1))

li1.insert(0,"a")
print("insert character into specific index: " + str(li1))

print("specific character count in list: ", li1.count('a'))

li1.pop(5)
print("delete elements from list: "+ str(li1))

li1.sort()
print("sort list: " + str(li1))

li1.extend(li2)
print("add li2 in li1 with extend: " + str(li1))




