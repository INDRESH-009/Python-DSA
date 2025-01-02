#hello world program 
print("Hello world")

#variables and datatypes 
x = 10
y = 12.34
name = "Indresh"
isPresent = True

#arithematic operators
a,b = 10,5;
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#comparision operators - result is a boolean
print(a>b)
print(a<b)
print(a>=b)
print(a>=b)
print(a==b)
print(a!=b)

#conditional statement 
x = 0
if(x>0):
    print("x is positive")
elif(x<0):
    print("x is negative")
else:
    print("x is 0")
    
#loops - for loop and while loop
for i in range(5):
    print(i)

count = 10
while(count>0):
    print(count)
    count -= 1

#functions 
def function_name(user_name):
    print(f'Good morning {user_name}')

function_name("Indresh") 


# datastructure

fruits = ["apple","banana","orange"]    #lists
person = {"name":"John", " age":20}     #dictionary
integers = (10,20,30,40,50)             #tuples
two_multiples = {2,4,6,8,10}            #sets

#I/O in python
name = input("Enter your name : ")
print(f'hello {name} thanks for the input')

 

