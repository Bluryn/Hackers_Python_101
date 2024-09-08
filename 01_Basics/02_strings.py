#########################
#Definition of a String #
#########################
String1 = "String =)"
String2 = 'Also string =)'

print(String1)
print(String2)

String3 = """Very 
Long 
String =)"""

print(String3)

String4 = "I\"m a string =)"
print(String4)

String5 = 'I\'m a string =)'
print(String5)

String6 = "I\"m a string\n I\"m on a newline =)"
print(String6)

String7 = "a" * 10
#Python is capable of multiplying strings
print(String7)

#We can also enumrate the number of characters
print(len(String7))

#We can also check if certain charcaters are ine the String
print("new" in String4) # Will returne False

#We can return if a String begins with a precise caracters
print(String6.startswith("L")) #Will return false
print(String6.startswith("I")) #Will return true

#We can also play with indexes for example when a characters appears in the string
print(String5.index("string")) #will return 6

#We can play with case
print(String5.upper())
print(String5.lower())

#Careful spaces are counted in a String
bordel_string= "    Messy String =( "
print(bordel_string)
#We have a function to clean the additionnal spaces in the string
print(bordel_string.strip())

#We can also replace a character within a string
print(bordel_string.replace("=(","=)").strip()) # We are also stripping

#We can split a string and specifiy a seperator
print(bordel_string.split()) #will find every words
print(bordel_string.split(",")) #will find every character chain between a ,
      
#New clean example
stringx = "new clean string ! Yeah"

#Here are some enteresting functions - encoding (used for exploits)
print(stringx.encode())
print(stringx.encode("utf-8")) #specified encoding

#We can play with alignement
print(stringx.rjust(25)) #it will add spaces so the string is 25 characters
print(stringx.rjust(25,"Y")) #spaces a replaces with Ys
      
#Concatenation
print("New" + "clean string ! Yeaj")
print("stringx" + str(len(stringx)) + " characters long")

print(1 + 1)
print("1" + "1")
print(type("1" + "1"))

#Here is an example of formating 
print("stringx is {} characters long!".format(len(stringx))) # {} is the place holder
print("{} {} {}".format(len(stringx), 4.0, 0x12)) #we can have multiple format place holder and print other variables
print("{0} {2} {1}".format)(len(stringx), 4.0, 0x12) # in this case we are specifying index for placeholders so that the order change
print("{length}".format(length=len(stringx)))# we can put a variable in the place holder
      

length = len(stringx)
print(f"stringx is {length} characters long") #other way of printing format
print("stringx is {length:.2f} characters long") #will output the lenght in float with 2 digit after decimal
# we can also print in binary, octo and hexidical ({length:b}, {length:x}, lenghth{o})