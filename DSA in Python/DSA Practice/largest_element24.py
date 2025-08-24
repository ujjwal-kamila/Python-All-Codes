# Find the largest element in an array 

class Solution:
    def find_largest(self,arr):
        n = len(arr)
        # large = arr[0]
        large = float("-inf")
        
        for i in range(0,n):
            if arr[i] > large:
                large = arr[i]
        return large



# test cases

ans = Solution().find_largest([1,-1,-5,6])
print(ans)
ans = Solution().find_largest([-1,-10,-8,-11])
print(ans)
