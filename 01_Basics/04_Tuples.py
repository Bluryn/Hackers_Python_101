#Tuples Definition
tuple_items = ("item1", "item2", "item3") #Tuples of Strings
print(tuple_items)
print(type(tuple_items)) #But still a Tuple
      
tuples_numbers = (1, 2, 3) #Tuples of Integer
print(tuples_numbers)
print(type(tuples_numbers)) #But still a Tuple

tuples_repeat = ('Combine!' ,) * 4  #Here we can repeat a string with a seperator
print(tuples_repeat)
print(type(tuples_numbers)) #But still a Tuple

#Append item

tuples_combined = tuple_items + tuples_numbers
print(tuples_combined) #Will print the 6 elements from the combined tuple
print(type(tuples_combined)) #Still a Tuple

#We can also unpack a tuple
item1, item2, item3 = tuple_items #if we add an "itemx" to the list it will fail because we only have 3 element in the tuple
print(item1)
print(item2)
print(item3)

#Evaluation 
print("item1" in tuple_items) #True
print("item2" in tuple_items) #True
print("itemx" in tuple_items) #False

#Counting and Index
print(tuple_items[0]) #item1
print(tuple_items[1]) #item2
print(tuple_items[2]) #item3
print(len(tuple_items)) #3
print(tuple_items[-1]) #Counting backwards #item3
print(tuple_items[-2]) #item2
print(tuple_items[0:2]) #extracting only a number of elements from 0 (included) until 2 (not included !!!)
print(tuple_items[:2]) #same as above
print(tuple_items[-3:-1]) #same here -1 is not included !!!

string1 = "i am a strongman !"
print(string1[0:4]) #"i am" (need to count space 0-3)
print(string1[-1])  #"!" last element 