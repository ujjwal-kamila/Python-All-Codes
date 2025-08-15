# Reverse an Array Using Recursion 

nums = [5,9,8,3,6,7,1,4,2]

# Best approach
def reverse_arr(nums, left, right):
    if left >= right:
        return
    
    nums[left], nums[right] = nums[right], nums[left]
    reverse_arr(nums, left + 1, right - 1)
    return nums

res = reverse_arr(nums, 5, 8)
print(res)

nums = [5,9,8,3,6,7,1,4,2]

# using slicing 
rev_arr = nums[::-1]
print("Using slicing",rev_arr)

# using reverse reversed() + list()
reverse_arr = list(reversed(nums))
print("using reverse +list",reverse_arr)


# Using .reverse() method
arr = [1, 7, 3, 8, 5]
arr.reverse()
print(arr) 


# using a for loop 
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1): #start, stop, step)
        reversed_arr.append(arr[i])
    return reversed_arr

# Example
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))


# reverse using while loop 
arr = [1,2,3,4,5]
left = 0
right = len(arr)-1
while left < right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right=-1
print(arr)