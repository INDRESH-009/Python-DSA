# Find the LCM of 2 numbers - smallest number that can divide both the numbers 
def lcm(a,b):
    small = a
    great = b
    if b<a:
        small = b
        great = a
    if great%small==0:
        sol = great
    else:
        sol = great*small
    return sol
print(lcm(4,6))


""" 
1. What is LCM and some examples 
2. Brute force method
3.
"""