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
Print(String6)

String7 = "a" * 10
#Python is capable of multiplying strings
Print(String7)

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

