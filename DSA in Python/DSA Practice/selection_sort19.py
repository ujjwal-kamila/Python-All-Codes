# Selection Sort in Python

# Assending order sorting 
class Solution:
    def selecton_sort(self,arr):
        n = len(arr)
        for i in range(0,n):
            min_index = i
            for j in range(i+1,n):
                if (arr[j] < arr[min_index]):
                    min_index = j
            arr[i],arr[min_index] = arr[min_index],arr[i]
        return arr # also can return arr[::-1] for decending


ans = Solution().selecton_sort([4,6,2,8,0,1])
print(ans)


# Decending order sorting 
class Solution:
    def selecton_sort(self, arr):
        n = len(arr)
        for i in range(0, n):
            min_index = i
            for j in range(i+1, n):
                if (arr[j] > arr[min_index]):  # Correct for descending
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

ans = Solution().selecton_sort([1,2,3,4,5,6,7,8,9,10])
print(ans)

