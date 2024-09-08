dict1 = {"a":1, "b":2, "c":3}
print(dict1)
print(type(dict1))
print(len(dict1))

print(dict1["a"]) #like list we cannot print 0 index elemet
print(dict1.get("a"))

print(dict1.keys())     # will be 'a', 'b', 'c'
print(dict1.values())   # will be 1 2 3
print(dict1.items())    # will be [('a',1),('b',2),('c',3)]

#Modify Value
dict1["a"] = 1          #print -> {'a':1, 'b':2, 'c':3}
dict1["d"] = 4          #print -> {'a':1, 'b':2, 'c':3, 'd':4}
dict1["a"] = 0          #print -> {'a':0, 'b':2, 'c':3, 'd':4}
dict1.update({"d":1})   #print -> {'a':1, 'b':2, 'c':3, 'd':4}

dict1.pop("d")          #will remove d key from dictionnary
del dict1['c']          #will remove c key from dictionnary

dict1['c'] = {"a":1, "b":2} #print = {'a':1, 'b':2, 'c':{'a':1, 'b':2}}

# We use dictionnary when we are not able to define in advance what will be the specific type of each variables