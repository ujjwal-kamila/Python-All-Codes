#  Quick Sort implementation in Python

class Solution:
    def quick_sort(self, arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            p_index = self.partition_arr(arr, low, high)
            # Recursively sort elements before and after partition
            self.quick_sort(arr, low, p_index - 1)
            self.quick_sort(arr, p_index + 1, high)

    def partition_arr(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1
            while j >= low + 1 and arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    
# test cases
arr = [10,9,8,6,5,4,1,2,3]
print("Original array = ",arr)
ans = Solution().quick_sort(arr,0,8)
print("\nSorted array = ",arr)
