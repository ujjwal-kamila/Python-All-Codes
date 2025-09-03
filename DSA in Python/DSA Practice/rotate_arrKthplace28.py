# Leetcode 189: Right Rotate an Array by K Places

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        for i in r