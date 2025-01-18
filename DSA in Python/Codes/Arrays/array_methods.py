# Let's create an array and apply all array methods
'''
append
count
extend
index
insert
pop
remove
reverse
'''

# Create an initial array
array = ['A', 'E', 'I', 'O']

# Create same array using list comprehension 
# array = [char for char in 'AEIO']


# Append 'U' to the array
array.append('U')
print("After appending 'U', the updated array is:", array)

# Count occurrences of 'A' in the array
count_A = array.count('A')
print("Count of 'A' in the array:", count_A)

# Extend the array with ['C']
array.extend(['C'])
print("After extending with ['C'], the updated array is:", array)

# Get the index of 'E'
get_index = array.index('E')
print("The index of 'E' is:", get_index)

# Insert 'Z' at index 2
array.insert(2, 'Z')
print("Array after inserting 'Z':", array)

# Pop the last element
pop_element = array.pop()
print("Array after popping the last element:", array)
print("Popped element is:", pop_element)

# Remove the first occurrence of 'Z'
array.remove('Z')
print("Array after removing 'Z':", array)

# Reverse the entire array
array.reverse()
# we can also use flip to reverse the array
#array = np.flip(array)
print("Reversed array is:", array)
