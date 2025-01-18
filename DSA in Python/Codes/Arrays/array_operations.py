# Create an Array in Python

import array as arr
new_arr = arr.array('i',[1,2,3,4,5])
print("The new array is : ",end = ' ')
for i in range (0,5):
    print(new_arr[i],end=' ')

print("\n")

# Create float array  
another_arr = arr.array('d',[1.5,2.5,5.0,6.8,8.9])
print("The float array is : ",end = ' ')
for i in range(0,4):
    print(another_arr[i],end= ' ')
    
# Insert at first 
new_arr.insert(0,10)
print("\nInsert 10 at first ,The new array is : ",end = ' ')
for i in range (0,6):
    print(new_arr[i],end=' ')


# Insert at the end
new_arr.append(20)
print("\nArray after inserting 20 at the end:",end=' ')
for i in range (0,7):
    print(new_arr[i],end=' ')
    
    
# Insert at specific position 
pos = 4
value = 100
new_arr.insert(pos,value)
print(f"\nArray after insertion {value} at position {pos}th : ",end =' ' )
for i in range (0,7):
    print(new_arr[i],end=' ')


# Deletion 
# Delet at first 

# display fun
def display_arr(array):
    for i in range (len(array)):
        print(array[i],end = ' ')

    
my_arr = arr.array('i',[1,3,5,6,8,9])
# main array
print("\nOriginal array is : ",end = ' ')
display_arr(my_arr)
print('\n')
# delet at first 
if len(my_arr) > 0:
    del_ele = my_arr.pop(0)
    print("Array after delet the first element :" ,end =' ')
    display_arr(my_arr)
    print("\nDeleted element is ",del_ele)

# delet from specific 
position = 1
if len(my_arr) > position:
    del_ele = my_arr.pop(position)
    print(f"Array after deleting from position {position} : ",end =' ')
    display_arr(my_arr)
    print("\nDeleted element is ",del_ele)



# delet from last
if len(my_arr) > 0:
    del_ele = my_arr.pop()
    print("Array after deleting last element : ",end = ' ')
    display_arr(my_arr)
    print("\nDeleted element is ",del_ele)