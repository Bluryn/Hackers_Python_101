#Definition of a Boolean
valid = True
not_valid = False

print(valid)
print(not_valid)            #These are not strings

#Evaluations
print(valid == True)        #will return True
print(not_valid == True)    #will return False
print(valid != True)        #will return False
print(not_valid != True)    #will return True

print(not valid)            #False
print(not not_valid)        #True #Carefule you can't use !valid => it is not a python valid syntax

#Other Evaulations
print((10 < 9) == True)     #False
print((10 == 10) == True)   #True
print((10 != 10) == True)   #False
print((10 >= 10) == True)   #True
print((10 >= 10) == True)   #True
print((10 > 9) == True)     #True

#Statement result
print(10 > 5 and 10 < 5)    #False
print(10 > 5 or 10 < 5)     #True

#Numeric Boolean
print(bool(0))              #False
print(bool(1))              #True
print(bool(0) == False)     #True
print(bool(1) == True)      #True