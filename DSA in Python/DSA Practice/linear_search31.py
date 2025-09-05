# Implementing Linear Search

'''
Given an array and a target value,
return the index of the target value if found,
otherwise return -1.
'''

def linearSearch(num, arr) -> int:
    for i in range(len(arr)):
        if arr[i] == num:
                return i
    return -1

print(linearSearch(3, [1, 2, 3, 4, 5]))  


# Linear Search Function
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:  
            return i
    return -1


# test case
arr = [10, 20, 30, 40, 50]
target = 30

res = linear_search(arr, target)

if res != -1:
    print(f"Element found at index {res} ")
else:
    print("Element not found")
