# 1800. Maximum Ascending Subarray Sum

from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Continue the ascending sequence
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)  # Update max sum
                current_sum = nums[i]  # Restart sum from current element        
        return max(max_sum, current_sum)

# Test Cases
print(Solution().maxAscendingSum([10,20,30,5,10,50]))  # ✅ 65
print(Solution().maxAscendingSum([10,20,30,40,50]))    # ✅ 150
print(Solution().maxAscendingSum([12,17,15,13,10,11,12]))  # ✅ 33
