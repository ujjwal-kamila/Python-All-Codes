# Leetcode 268: Find Missing Number in an Array

# brute force approach
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i 
            
            
nums = [3,0,1]
sol = Solution()
ans = sol.missingNumber(nums)
print(ans)

# better solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        freq={}
        for i in range(0,n+1):
            freq[i]=0
        
        for num in nums:
            freq[num]=1
        
        for key,val in freq.items():
            if val ==0:
                return key
            
            
nums = [1,2,3,4]
sol = Solution()
ans = sol.missingNumber(nums)
print(ans)


# optimal solution n.n(n+1)//2 -sum of nums
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        total = n* (n+1) //2
        return total-sum(nums)
            
            
nums = [0,2,3,4]
sol = Solution()
ans = sol.missingNumber(nums)
print(ans)
