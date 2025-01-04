# create a new list where each element is the square of the corresponding element in the input list 

def square(arr):
    result = []
    for num in arr:
        result.append(num**2)
    return result
print(square([2,3,4,5]))