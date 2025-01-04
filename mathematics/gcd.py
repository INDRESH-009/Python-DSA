# Find the hcf or gcd of 2 numbers

""" 
Points to remember :
lets assume  2 numbers 4,6 : 
    GCD is always less than or equal to the smallest number 
    if smallest number 

"""
def gcd(a,b):
    small = a
    great = b
    if b<a:
        small = b
        great = a
    sol = 1
    if(great%small==0):
        sol = small
    else:
        for i in range(small-1,1,-1):
            if(great%i==0 and small%i==0):
                sol = i
                print(sol)
                break
    return sol
print(gcd(40,200))
            