#  Leetcode 283: Move Zeros to the End of the List

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = []
        zeros = []
        for num in nums:
            if num ==0:
                zeros.append(0)
            else:
                l.append(num)
            
        nums[:] = l+zeros


sol =Solution()
nums = [0,1,0,3,12]
res = sol.moveZeroes(nums)
print(nums)



# Optimal using two pointer 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0  # pointer for placing non-zero elements
        # Move all non-zero elements forward
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        # Fill remaining positions with zeros
        for i in range(j, n):
            nums[i] = 0

        
sol =Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)

# optimal 

