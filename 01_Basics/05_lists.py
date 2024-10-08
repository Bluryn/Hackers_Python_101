##################
#List Definition #
##################
list1 = ["A", "B", "C", "D" , "E", "F"]
print(list1)

list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]
print(list2)
print(type(list2))

#############
#Indexation #
#############
print(list1[0])
print(list1[-1])

print(list2[3][0])      # will return the third element from the list counting from the beginning
print(list2[3][-1])     # will return the third element from the list counting from the end

#Lists can be change thereafter
list1[0] = "X"
print(list1) # X will replace A

#We can also delete /add from /to list
del list1[0] # will delete first element of list 1
print(list1) # list will begin with B
list1.insert(0, "A") #insert to list 1 at index 0 the string A
print(list1) 
del list1[0]
list1 = ["A"] + list1 #will add the list with A into the list, always in front
print(list1) # here it's like re-adding the letter A to list
list1.append("G")   #will add G at the end of the list

###########
#Counting #
###########
print(max(list1))               # will return the maximum value (G)
print(min(list1))               # will return the minimum value (A)
print(list1.index("C"))         # will verify the index of the desired element of the list
print(list1[list1.index("C")])  # will return the element of the list1 at the index of the desired element of the list1
list1.reverse()                 # Obvious function
list1 = list1[::-1]             # slice method exploitation to reverse the list
print(list1.count("A"))         # will count how many time A occurs
list1.pop()                     # will pop off the last element of the list

#Other useful functions 
list3 = ["H", "I", "J"]
list1.extend(list3)             # will extend list 1 with list 3
list1.clear()                   # will clear all element of the list
list4 = [8, 12, 5, 6, 17, 2]
list4.sort()                    # will sort the list
list4.sort(reverse=True)        # will reverst sort the list

#We can't copy list :
# ex :
list5 = list4
print(list4)
print(list5)

list5[2] = "X"
print(list5)                    # 5 will be replace by X
print(list4)                    # 5 will also be replace by X because there list 5 is referenced to 4 not copied !
# to avoid this, we need to use the copy() function

list6 = list4.copy()
list6[2] = "A"
print(list6)                    # third value will be A (replaces X)
print(list4)                    # third value will still be X

list7 = ["1", "2", "3"]
list8 = list(map(float, list7))
print(list8)                    # all mapped element, so integers will be mapped to corresponding float