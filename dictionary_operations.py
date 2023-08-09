dict1={'a':'aa','b':'bb','c':'cc',3:33 ,5:55, True: True,
       "list":["l1","l2","l3"],(1,2,3):("t1","t2","t3"),"set":{"s1","s2","s3"}}

print("Print original dictionary: " +str(dict1))
print("Get all keys from dictionary: " + str(dict1.keys()))
print("Get all values from dictionary: " + str(dict1.values()))

print("Fromkeys operations:")
x = ('key1', 'key2', 'key3')
y1 = 0
y2=[1,2,3]
dict2 = dict.fromkeys(x, y1)
print(dict2)
print(dict.fromkeys(x,y2))

print("dict items: " + str(dict1.items()))

print("Update dictionary operations: ")
dict1.update({3:10})
print(dict1)
dict1.update({4:44})
print(dict1)

