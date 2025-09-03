# Leetcode 189: Right Rotate an Array by K Places

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)