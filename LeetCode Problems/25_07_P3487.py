# 3487. Maximum Unique Subarray Sum After Deletion

from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sum = 0
        for i in set(nums):
            if i >0:
                sum +=i
        if sum ==0:
            return max(nums)
        return sum

nums = [-100]
sol = Solution()
print(sol.maxSum(nums)) 


            