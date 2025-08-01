#2419. Longest Subarray With Maximum Bitwise AND


from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = 0
        current = 0

        for num in nums:
            if num == max_val:
                current += 1
                longest = max(longest, current)
            else:
                current = 0

        return longest


res = Solution().longestSubarray([1,2,3,3,2,2])
print(res)