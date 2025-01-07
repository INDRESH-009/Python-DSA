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

7. .remove(x) - remove the value x from the list , produces error if we try to remove a value thats not in list

8. .pop() - removes the last element of the list 
9. .pop(i) - removes the value from that index

10. del list_name[i] - del is a general purpose keyword that can be used on any objects , it deletes the item from the given index
11. del list_name[i:j] - it can also delete items if a range of index is given i is inclusive and j is exclusive
 
12. max(list_name) - gives the max value 
13. min(list_name) - gives the min value
14. sum(list_name) - gives the sum of the elemnts in the list
15. .reverse()     - reverses the list items
16. .sort()        - sorts the elements of the list 
                     If the elemnts of the list is not purely numeric and contains strings then it doesnt work
                     If the entire list contains strings then it sorts based on the lexicographic order

"""

list2 = [10,20,30,40,50]
list2.append(30)            # append()
print(list2)
list2.insert(0,5)           # insert()
print(list2)
print(20 in list2)          # x in listname
print(list2.count(30))      # count() method
print(list2.index(30))      # index() method
print(list2.index(30,4,7))  # index(x,i,j) method - i inclusive and j exclusive

print("list before remove method",list2)
list2.remove(40)
print("mutated list",list2)

print("\npop function")
list2.pop() #removes last value 30
print(list2)

print("\npop from index 2")
list2.pop(2)
print(list2)

print("\nUsing the delete function to remove value from index 2")
del list2[2]
print(list2)

print("\nUsing del to remove range of indeces from 0 to 2 - viz(0,1)")
del list2[0:2]
print(list2)

list3 = [5,10,105,200,30]
print("\n\nlist is - ",list3)
print("max value",max(list3))
print("min value",min(list3))
print("sum value",sum(list3))
print("reversed list")
list3.reverse()
print(list3)


print("sorted list")
list3.sort()
print(list3)

""" 
list4 = [10,20,"hello",50]
list4.sort()
print(list4) 
----------------> Provides error
"""

print("\n\nSorting strings lexicographically")
list4 = ["a","d","f","b"]
list4.sort()
print(list4)

list5 = ["ab","aa","zc","bz"]
list5.sort()
print(list5)



