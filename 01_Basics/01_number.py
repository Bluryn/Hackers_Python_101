tl_int = 1
tl_float = 1.0

print(tl_int)           # 1
print(tl_float)         # 1.0
print(type(tl_int))     # <class 'int'>
print(type(tl_float))   # <class 'float'>

tl_complex = 3.14j
print((tl_complex))     # 3.14j
print(type(tl_complex)) # <class 'complex'>

tl_hex = 0xa
print(tl_hex)           # 10
print(type(tl_hex))     # <class 'int'>
#why so -> we count in base 10 so python will adapt

tl_octal = 0o10
print(tl_octal)          # 8
print(type(tl_octal))    # <class 'int'>
#same as above

print(1 + 0x1 + 0o1)     # 3

#Absolute value
print(abs(2))            #2
print(abs(-2))           #2

#Round
print(round(3.4))        #3
print(round(3.5))        #3
print(round(3.6))        #4

#Binary
print(bin(8))            #0b1000

#hexadecimal
print(hex(8))            #0x8
