# Leetcode 189: Right Rotate an Array by K Places

from typing import List
# brute force 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % n
        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)
        # # using slicing
        # n =len(nums)
        # k = k % n
        # nums[:] = nums[n-k:] + nums[:n-k]



class Solution:
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        """
        Reverse the portion of nums starting at index l up to index r in-place.
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        # 1. Reverse the last k elements
        self.reverse(nums, n - k, n - 1)
        # 2. Reverse the first n-k elements
        self.reverse(nums, 0, n - k - 1)
        # 3. Reverse the whole array
        self.reverse(nums, 0, n - 1)

        