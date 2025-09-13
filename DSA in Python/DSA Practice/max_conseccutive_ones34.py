# Leetcode 485: Max Consecutive Ones

'''
Have an arr with no of 1's find max number of consecutive 1's
'''

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(0,n):
            if nums[i] == 1:
                count +=1
    
            else:
                max_count = max(max_count,count)
                count =0
        # return max_count  # works whne last num is 0
        return max(max_count,count)  # if last max 1s with no 0's then not reset count
    
sol = Solution()
print("Max Consecutive 1's is :",sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print("Max Consecutive 1's is :",sol.findMaxConsecutiveOnes([1,1,0,1,1,1,1,0]))


# another approach using list
'''
store count in a list and return max 
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        count=0
        for num in nums:
            if num == 0:
                res.append(count)
                count = 0
                
            else:
                count +=1
        res.append(count)
        return max(res)
    
    
sol = Solution()
print("Max Consecutive 1's is :",sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print("Max Consecutive 1's is :",sol.findMaxConsecutiveOnes([1,1,0,1,1,1,1,0]))