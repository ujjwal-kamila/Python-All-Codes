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

        for _ in range(0,rotations):
            last = nums.pop() 
            nums.insert(0, last) 
        
    

# better using slicing 
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Rotates the array to the right by k steps.
        """
        n = len(nums)
        k = k % n   # handle if k > n
        nums[:] = nums[n-k: ] + nums[ :n-k]   # slicing



# Optimal Leetcode 
from typing import List

class Solution:
    def reverse(self, arr: List[int], l: int, r: int) -> None:
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.
        """
        n = len(nums)
        k = k % n  # handle if k >= n

        # Step 1: Reverse the last k elements
        self.reverse(nums, n-k, n-1)

        # Step 2: Reverse the first n-k elements
        self.reverse(nums, 0, n-k-1)

        # Step 3: Reverse the whole array
        self.reverse(nums, 0, n-1)
