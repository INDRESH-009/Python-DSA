# Slicing can be done in list , tuple and string
# list[start:stop:step] - we cut a list from the index of start to index of stop where start index is included and stop index is excluded , if step is not given it is taken  as 1 by default

l = [10,20,30,40,50,60,70,80,90,100]
#slice this list from index 3 to 6 stepping with 1 
print(l[3:6:1])
#slice this list from index 0 to 5 stepping with 2 
print(l[0:5:2])
#slice from start to index 4 
print(l[:4])
#slice from index 3 to end
print(l[3:])
#slice form index 2 to 6
print(l[2:6])
# slice using negative step - from 4th index to 1st index stepping down by 1
print(l[4:1:-1])
# splicing using negative indexing - (-1 at last ) and (-10 at first for the above list)
""" 
_________________________________________
|___|___|___|___|___|___|___|___|___|___|
  0   1   2   3   4   5   6   7   8   9
 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
 """
print(l[-10:-1:1])
print(l[-1:-6:-1])

# to reverse a list use the following 
print(l[ : :-1])
# to get the whole list 
print(l[:])


# Slicing in list , tuple and string
""" 
We will create a copy of a list, tuple, and string using slicing, storing the copied values in new variables. Then, we will check whether the new variables reference the same object as the originals or if a new copy has been created.
"""

# creating a copy of l1 and storing in l2 : Slicing in lists creates a new list object (shallow copy).
l1 = [10,20,30]
l2 = l1[:]

# Slicing in tuples and strings does not create a new object; it simply references the original object.

t1 = (10,20,30)
t2 = t1[:]

s1 = "Indresh"
s2 = s1[:]

print(l1 is l2) # no they are different objects
print(t1 is t2) # they refer to the same object
print(s1 is s2) # they refer to the same object

# The is operator in Python checks object identity, meaning it determines whether two variables refer to the same object in memory.