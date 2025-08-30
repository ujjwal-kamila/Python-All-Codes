# 35. Search Insert Position


from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] >= target:
                return i
        return n

sol = Solution()
print(sol.searchInsert([1,3,5,6],5))
print(sol.searchInsert([1,3,5,6],2))
print(sol.searchInsert([1,3,5,6],7))