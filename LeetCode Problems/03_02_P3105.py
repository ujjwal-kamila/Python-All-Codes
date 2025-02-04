# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray

'''
You are given an array of integers nums. Return the length of the longest 
subarray of nums which is either strictly increasing or strictly decreasing
'''

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        inc = dec = 1
        max_len = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec += 1
                inc = 1
            else:
                inc = dec = 1  # Reset on equal elements            
            max_len = max(max_len, inc, dec)
        return max_len
    
sol = Solution()
print(sol.longestMonotonicSubarray([1, 4, 3, 3, 2])) 
print(sol.longestMonotonicSubarray([3, 2, 1]))      

