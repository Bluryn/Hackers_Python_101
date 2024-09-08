##########################
#Definition of a Boolean #
##########################
valid = True
not_valid = False

print(valid)
print(not_valid)            #These are not strings

##############
#Evaluations #
##############
print(valid == True)        #will return True
print(not_valid == True)    #will return False
print(valid != True)        #will return False
print(not_valid != True)    #will return True

print(not valid)            #False
print(not not_valid)        #True #Carefule you can't use !valid => it is not a python valid syntax

####################
#Other Evaulations #
####################

print((10 < 9) == True)     #False
print((10 == 10) == True)   #True
print((10 != 10) == True)   #False
print((10 >= 10) == True)   #True
print((10 >= 10) == True)   #True
print((10 > 9) == True)     #True

###################
#Statement result #
###################
print(10 > 5 and 10 < 5)    #False
print(10 > 5 or 10 < 5)     #True

##################
#Numeric Boolean #
##################
print(bool(0))              #False
print(bool(1))              #True
print(bool(0) == False)     #True
print(bool(1) == True)      #True

############
#Operators #
############
print(10 + 10)              #20
print(10 - 10)              #0
print(10 / 10)              #1.0
print(10 // 10)             #1
print(10 / 3)               #3.33333333
print(10 // 3)              #3
print(10 * 10)              #100
print(10 ** 10)             #10^10
print(10 % 10)              #0

###########################
#Definition with variable #
###########################
x = 10
print(x)                    #10
x = x + 1
print(x)                    #11
x+=1
print(x)                    #12
x-=1
print(x)                    #11
x*=5
print(x)                    #55
x/=5
print(x)                    #11.0

#########
#Binary #
#########

x = 13
print(bin(x))               #0b1101
print(bin(x)[2:].rjust(4,"0"))     #1101 #[2:] allow to remvoe the 0b (first 2 digit) and rjust is here so that the value is always going to be four bits length
y=5
print(bin(x)[2:].rjust(4,"0"))     #0101 

#Binary bitwise output check #Bitwise operator works differently

print(bin(x & y)[2:].rjust(4,"0")) #0101
print(x & y)                       #5
print(bin(x | y)[2:].rjust(4,"0")) #1101

#Bit shifts

print(bin(x >> 1)[2:].rjust(4,"0")) #0110 (we can't see all digits since it justified (4))
print(bin(x >> 2)[2:].rjust(4,"0")) #0011
print(bin(x >> 3)[2:].rjust(4,"0")) #0001
print(bin(x >> 4)[2:].rjust(4,"0")) #0000
print(bin(x << 1)[2:].rjust(4,"0")) #11010

#Those operations comes handy when you can't understards an exploit and you have to break it down in python
