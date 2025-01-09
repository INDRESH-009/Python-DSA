# Take a list as input and give 2 output list - one having all the even elements of that list and the other havong all the odd elements of the list 

def fun(list):
    even = []
    odd = []
    for i in range (len(list)):
        if (list[i]%2==0):
            even.append(list[i])
        else:
            odd.append(list[i])
    print(even)
    print(odd)
    return 0
fun([1,2,3,4,5])