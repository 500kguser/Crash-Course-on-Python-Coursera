#Conversion Types

#Implicit Conversion
print("An implicit converstion is when Python automatically changes one data type, to another.")
print("For example: '10 + 10.5' results in an implicit conversion.")
print("When Python adds an integer to a float. Python converts the integer to a float.")
print("For example: ")
a = 10
b = 10.5
print(a + b)
print(type(a + b))

#Explicit Conversion
print("Alternatively, an explicit conversion is when you manually set a data type.")
print("For Example: Adding a data type name, such as 'str()', it changes the type.")
print("Below, I am adding the integer 10 to a variable, but explicitly setting it to a string.")
print("For example: ")
c = str(10)
print(type(c))