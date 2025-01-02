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

n = 10
for i in range (n):
    print(nth_fibo_term(i) , end=" ")
    