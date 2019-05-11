#!/usr/bin/python

############ Specify a Variable Type ############

#https://www.w3schools.com/python/

#	** There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

### Casting in python is therefore done using constructor functions:

#int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)

#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


print ("Examples For Integers ::-") 
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print (x)
print (y)
print (z)
#print "\n"

print ("Examples For Floats ::-")
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print (x)
print (y)
print (z)
print (w)
#print "\n"
print ("Examples For Strings ::-")
x = str("A1") # x will be 's1'
y = str(5319)    # y will be '2'
z = str(5319.0)  # z will be '3.0'
print (x)
print (y)
print (z)
