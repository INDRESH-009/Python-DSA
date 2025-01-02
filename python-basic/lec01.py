#take an input n from the user and write a function which return the sum of the first n natural numbers 

num = input("Enter the number n : ")    #input return str
num = int(num)                          #convert str to int
def sum_of_first_n(n):
    sum = 0
    for i in range(1,n+1):              #doesnt include last num
        sum += i
    return sum
print(sum_of_first_n(num))
