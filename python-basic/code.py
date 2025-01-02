# The core datatypes in python are - Int , Float , String , Bool
# Varibales in python are dynamically typed and does not need any declaration with datatype like C or C++ 
a = 10
b = 10.23
c = "Hello"
d = True

# dynamic typing 
d = "Now I am a string"

# assigning values of one variable to another - a becomes "hello" and c remains as it is 
a = c 
print (a)
print (c)

# printing in python
print("Hello world")    # strings in print statement shd be in braces 
print(10)
print(2.4)
# printing varibales 
print(a)
print(d)
print(c)
# printing multiple items in a print statement 
print('hello',10,'isTrue',True,2.5)     # seperated by commas 
# end parameter in print statement 
# end parameter tells what to do after this print statement , default - end = \n 

# ends with | 
print('hello',10,True,'ok',end='|')
print("next line")
# ends with newline
print("hello",end="\n")
print("next line")
# ends with tab space
print("hello",end="\t")
print("next line")

# Getting input in python - we get input using input('prompt') function
name = input('Enter your name : ')
age = input('Enter your age : ')
print("Hello",name,"you are",age,"years old")

# Arithematic operator
x = 5
y = 3
summ = x + y
diff = x - y
mul = x * y
div = x / y
int_result_ofdiv = x // y
expo = x**y
mod = x % y
print(summ,diff,mul,div,int_result_ofdiv,expo,mod)