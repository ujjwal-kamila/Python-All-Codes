<<<<<<< HEAD
# Quick Sort: Divides the array into smaller sub-arrays around a pivot.
=======
>>>>>>> e692ec2e00e5c2e57a6d26a963e32e5a4cab6842
# Quick sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
print("Quick Sorted array:", quick_sort(arr))
