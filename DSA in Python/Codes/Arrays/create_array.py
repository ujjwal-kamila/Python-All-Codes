# How to create a array in python

#using array modules

import array as arr
my_ar = arr.array('i',[1,3,2,4,5,6,8,7])

# Or we can import as "from array import *"
from array import *
my_array =array('i',[1,3,2,4,5,6,8,7])
print(type(my_array))

# printing array elements using loop
print("Array elements")
for i in range(len(my_array)):
    print(my_array[i],end=' ')
    
print("\n")

# or we can use as for loop to direct array name
for i in my_array :
    print(i,end=' ')

print("\n")

# using while loops
i = 0 
while (i < len(my_array)):
    print(my_array[i])
    i +=1
    

# using  numpy 
import numpy as np

### Creating a numpy array
my_array = np.array([1, 2, 3, 4, 5])
print(type(my_array))  
print(my_array)  


# Create an array using numpy
import numpy as np
a = np.array([1,2,3,4,5,6,7,8])
print("Array is :",a)

# 2d array using numpy
b = np.array([[1,2,3,4],[4,6,8,9]])
print("Array is :",b)

# # 1d array with two list types 
# c = np.array([[1,2,3],[1,8]])
# # gives error as inhomogenous part 
# print("Array is :",c)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Iterating over the matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()