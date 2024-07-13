####################
#Simple declaration#
####################
name = "name" # declaratio of a string
print(name)

name_length = 4 #declarition of an integer
print(name_length)

name, name_length = "name" , 4 #In-line declaration of multiple variables

print(type(name)) #Python will try to guess the type (string)
print(type(name_length)) #Python will try to guess the type (integer)

#################################
#Specify type within declaration#
#################################
name_length = "4" #Here it a string !   
print(type(name_length)) #will return <class 'str'>

name_length = int("4") #Here it an integer !   
print(type(name_length)) #will return <class 'int'>

name = int("name") #Here if we print we will get an error

##################
#Case sensitivity#
##################

name_length = 4
Name_length = 5
# if we print those variables it will return 4 and 5 -> not the same !!!

##################
#List declaration#
##################

name_list = ["name", "oui", "non"]
print(type(name_list)) # will return <class 'list'>

name1, name2, name3 = name_list #It will assign in order the values in the list for each variable
#we can print them separately
print(name1)
print(name2)
print(name3)

###################
#Tuple declaration#
###################

name_tuple = ("name", "oui", "non")
print(type(name_tuple)) #will print <class 'tuple'>

###################
#Tuple dictionnary#
###################

name_dictionnary = {"name", "oui", "non"}
print(type(name_dictionnary)) #will print <class 'dictionnary'>

###############
#Tuple boolean#
###############

name_boolean = True
print(type(name_boolean)) #will print <class 'bool'>

#############
#Tuple range#
#############

name_range = range(6)
print(type(name_range)) #will print <class 'range'>

#############
#Tuple bytes#
#############

name_bytes = b"name"
print(type(name_bytes)) #will print <class 'bytes'>

print(name_tuple)       # ("name", "oui", "non")
print(name_list)        # ["name", "oui", "non"]
print(name_dictionnary) # {"name", "oui", "non"}
print(name_boolean)     # True
print(name_range)       # range(0,6)
print(name_bytes)       # b'name'

