# 3151. Special Array I  ...Check if an Array is Special
'''
You are given an array of integers nums. 
The array is considered special if every adjacent pair of elements contains one even and one odd number.
Return True if the array is special, otherwise return False.
'''

# Input: nums = [2,1,4]
# Output: true

# (2,1) → Even, Odd 
# (1,4) → Odd, Even 
# Since all pairs have different parity, the array is special so True

'''
Approachh:
Iterate through the array and check each adjacent pair.
If any adjacent pair has the same parity (both even or both odd), return False.
If all pairs have different parity, return True.'''

from typing import List
class Solution:
    def isArraySpecial(self,nums:List[int]) -> bool:
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:  # Both even or both odd
                return False
        return True

# Test Cases
print(Solution().isArraySpecial([1]))  
print(Solution().isArraySpecial([2,1,4]))
print(Solution().isArraySpecial([4,3,1,6]))  
print(Solution().isArraySpecial([1,4,3,8]))  