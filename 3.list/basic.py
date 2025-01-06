""" 
speciality of list - random access 
helps in storing collection of items , it uses array internally
It is dynamic in size , grows and shrinks in size 
it can hold differet types of items in the same list 
Supports both positive and negative indexing
"""
l = [10,20,"numbers",True,2.43]

print(l[0])
print(l[-5])

print(l[1])
print(l[-4])

print(l[2])
print(l[-3])

print(l[3])
print(l[-2])

print(l[4])
print(l[-1])

print(l)

""" 
builtin methods for list 
1. .append(x) - appends the item x to the last of the list 
2. .insert(index,x) - inserts item x at the goven index
3. x in list_name - in method checks if the item x is present in the list mentioned - value outputted is a boolean
4. .count(x) - tells how many occurances of the item x is present in the list 
5. .index(x) - talkes the item and returns the index of its first occurance in the list
6. .index(x,i,j) - another way of using the index method where it takes a element as argument , takes 2 index i(start index viz inclusive) and j(end index viz exclusive)
7. 
"""