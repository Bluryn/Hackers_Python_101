#########################
#Conditional Definition #
#########################

#########
# Basic #
#########
#
if True:
    print("True")           #Return "True" -> because it's True that it is True
if False:
    print("False")          #Return None -> because it's False that it is False
if not False:
    print("not False")
#
if 1 < 1:
    print("1 < 1")          #Return None -> because 1 <= 1 -> so next step
elif 1 <= 1:
    print("1 <= 1")         #Return "1 <= 1" -> because 1 <= 1
else:
    print("else 1")         #Fall back if none of above are met

#
if 1 < 1:
    print("1 < 1")          #Return None -> because 1 <= 1 -> so next step
elif 1 <= 1:
    print("1 <= 1")         #Return "1 <= 1" -> because 1 <= 1
else:
    print("else 1")         #Fall back if none of above are met

#
if 1 < 1:
    print("1 < 1")          #Return None -> because 1 <= 1 -> so next step
elif 1 <= 1:
    print("1 <= 1")         #Return "1 <= 1" -> because 1 <= 1
elif 2 < 2:
    print("2 < 2")          #If condition above was not met -> it will not trigger because it's False + there is no fall back

#
if 1 < 1:
    print("1 < 1")          #Return None -> because 1 <= 1 -> so next step
elif 1 <= 1:
    print("1 <= 1")         #Return "1 <= 1" -> because 1 <= 1
elif 2 < 2:
    print("2 < 2")          #If condition above was not met -> it will not trigger because it's False + there is no fall back

##################
# With Operators #
##################
#
if 1 > 0 and 0 < 1:
    print("1 > 0 and 0 < 1")          #Return "1 > 0 and 0 < 1" -> because it's True
#
if 1 < 0 and 0 < 1:
    print("1 < 0 and 0 < 1")          #Return None -> because one the two statement is False
#
if 1 < 0 or 0 < 1:
    print("1 < 0 and 0 < 1")          #Return "1 < 0 and 0 < 1" -> because one the two statement is True
#
if (1 < 0 or 0 < 1) or 1 == 0 :
    print("1 < 0 and 0 < 1")          #Return "1 < 0 and 0 < 1" -> because one the two statement is True

###############
# Combination #
###############

#
if 0 < 1: print("0 < 1")
print("1 >= 1") if 1 >= 1 else print("1 < 1") # Return "0 < 1" and "1 >= 1"
