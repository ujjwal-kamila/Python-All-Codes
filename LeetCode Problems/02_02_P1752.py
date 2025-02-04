# 1752. Check if Array Is Sorted and Rotated

from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
    
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Compare with next element
                count += 1
            if count > 1:
                return False  # More than one break in order, not sorted & rotated
        
        return True

# Test cases
print(Solution().check([3, 4, 5, 1, 2]))  
print(Solution().check([2, 1, 3, 4]))     
print(Solution().check([1, 2, 3]))     
        
