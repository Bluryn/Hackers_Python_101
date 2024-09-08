#Simple Definition
set1 = {"a", "b", "c"}
print(set1)                 #run this multiple time and you'll see that sets doesn't have any particular order with
print(type(set1))

set2 = {"a", "a", "a"}
print(set2)                 #will only print {'a'} because it's a unique value
print(len(set2))            #as define above -> will return 1

set3 = {"a", 0, True}
print(set3)                 #Will print all of it
set4 = {"b", 1, False}
print(set4)                 #Will print all of it

# Modify Value
set1.add("d")
print(set1)                 #Will return {'a','b','c','d'} in no particular order

set3.update(set4)           #Here we are update set 3 with set 4
print(set3)                 #Will return {'a',0,True,'b'} => Because 0=FAlse and 1=True so duplicate -> it will only keep one of each and in no particular order

# Combination
list1 = ["a", "b", "c"]     # ['a', 'b', 'c']
set4  = {4, 5, 6}           # {4, 5, 6}
set4.update(list1)         
print(set4)                 # Will return {4, 5, 6, 'a', 'b', 'c'}

# Remove

set4.remove(1)
print(set4)                 # Will return an error because value 1 is not in the set

set4.remove(4)
print(set4)                 # Will return {5, 6, 'a', 'b', 'c'}

set4.remove(4)
print(set4)                 # Will return an error because value 5 is no longer in the set

set4.discard(4)
print(set4)                 # Will return {5, 6, 'a', 'b', 'c'} -> no error

set4.pop
print(set4)                 # Will return the set with a random item removed

#Set is a good data structure if you don't care about the order and when you don't want to work with duplicates