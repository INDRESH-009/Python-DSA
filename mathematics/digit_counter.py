# For a given number find the number of digits in it 
def num(n):
    count = 0
    while n > 0:
        n = n//10
        count = count+1
    return count
print(num(12312))