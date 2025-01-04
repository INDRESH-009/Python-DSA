# Find the factorial of a number

def fact(n):
    res = 1
    while n>0:
        res = res*n
        n = n-1
    return res
print(fact(5))

# Recursive solution
def fact2(n):
    if n<=0:
        return 1
    return n*fact(n-1)
print(fact2())