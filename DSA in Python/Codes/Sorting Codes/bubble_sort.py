#Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order. 
# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Bubble Sorted array:", arr)

