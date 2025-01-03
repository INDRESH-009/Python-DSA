# write a recursive solution for factorial of a number 
def fact(n):
    if(n<=0):
        return 1
    return n*fact(n-1)

print(fact(2))

# nth fibonacci where n>=0
# fibonacci - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, - each number is sum of the preceeding 2 numbers 

def nth_fibo_term(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return nth_fibo_term(n-1) + nth_fibo_term(n-2)

n = 3
for i in range (n):
    print(nth_fibo_term(i) , end=" ")
    
    
    
# Sum of digits using recursion , n is input - n=5 ---- 1+2+3+4+5 = 15
def sum(n):
    if(n<=0) :
        return 0
    return n+sum(n-1)
print(sum(5))

# Sum of digits within a number using recursion , n is input - n=215 ---- 2+1+5 = 8
def sum_of_digit(n):
    if n<10:
        return n
    return n%10 + sum_of_digit(n//10)
print(sum_of_digit(10))

