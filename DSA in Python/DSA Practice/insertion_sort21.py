# Insertion Sort in Python
# picking each element and placing it in its correct position

class Solution:
    def insertion_sort(self,arr):
        n = len(arr)
        for i in range(1,n):
            key=arr[i]
            j = i-1
            while j>=0 and arr[j]>key:
                arr[j+1] = arr[j]
                j-=1
            # Place 'key' into its correct spot
            arr[j+1] = key
        return arr


ans = Solution().insertion_sort([4,6,2,8,0,1])
print(ans)
