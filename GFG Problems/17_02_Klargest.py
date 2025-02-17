# k largest elements

class Solution:
    def kLargest(self, arr, k):
        ans = []
        arr.sort(reverse=True)  
        
        for i in range(k):  
            ans.append(arr[i])
        
        return ans

# Test Case
sol = Solution()
print(sol.kLargest([12, 5, 787, 1, 23], 2))
print(sol.kLargest([1, 23, 12, 9, 30, 2, 50], 3))
