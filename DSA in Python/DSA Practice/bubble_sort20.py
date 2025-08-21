#  Bubble Sort in Python 

# Assending order sorting 
class Solution:
    def bubble_sort(self,arr):
        n = len(arr)
        for i in range(n-2,-1,-1):
            for j in range(0,i+1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr


# Testing
arr = [5, 8, 1, 6, 9, 2, 4]
print("Original : ", arr)

ans =Solution().bubble_sort(arr)

print("Sorted : ", ans)






# "Best case "
# class Solution:
#     def bubble_sort(self, arr):
#         n = len(arr)
#         for i in range(n-1):
#             swapped = False       
#             for j in range(0, n-i-1):   
#                 if arr[j] > arr[j+1]:
#                     arr[j], arr[j+1] = arr[j+1], arr[j]
#                     swapped = True
#             if not swapped:        # if no swap-> array is sorted
#                 break
#         return arr
