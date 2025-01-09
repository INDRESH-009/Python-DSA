# write a py function that takes a list and value x as input and returns a list whose elemenst are smaller than the input element x

def fun(l,x):
    smaller = []
    for i in range(len(l)):
        if(l[i]<x):
            smaller.append(l[i])
    return smaller
print(fun([10,20,30,40,50],35))
