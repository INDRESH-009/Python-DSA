# Check if a given number is palindrome - when read from both sides it should be same 

def isPal(n):
    rev_num = 0
    temp = n
    while temp!=0:
        last_digit = temp%10
        rev_num = rev_num*10 + last_digit
        temp = temp//10
    return rev_num==n

print(isPal(1221))