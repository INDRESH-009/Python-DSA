import sys
print(sys.version)
if 5<2:
    print("5 greater than 2")
else:
    print("2 greater than 5")
#single line comment 
'''
String literals which are not assigned to a variable is not considered by python so it can be used as a multiline comment
'''

#variabls - no need declaration and dynamically typed 
x = "Indresh"
y = 20
z = True
#x can also hold integer and y can hold string , dynamic typing
x = 20
y = "Indresh"
#type casting 
x = str(100) #100 becomes '100'
print(x)
print(type(x))

y = int('3') #'3' becomes 3
print(y)
print(type(y))

z = float(4) # 4 becomes 4.0
print(z)
print(type(z))

#Assigning multiple values to multiple variable
a,b,c = "Apple" , "Ball" , "Cat"
print(a)
print(b)
print(c)
#Assigning one value to multiple varaibles 
a = b = c = "Alphabets"
print(a)
print(b)
print(c)
#Unpacking a collection - If you have a collection of values in list or tuple then you can extract these values into variables 
fruits = ["Grapes","Orange","Papaya"]
a,b,c = fruits
print(a)
print(b)
print(c)
