# 2425. Bitwise XOR of All Pairings

# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
# Explanation:
# A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
# The bitwise XOR of all these numbers is 13, so we return 13.

'''
Explanation:
If one array has an odd length, XOR all elements from the other array.
If both arrays have an even length, skip XOR operations as they cancel out.
'''

'''
Approach:
1Initialize result = 0.
2.XOR all elements of nums1 if len(nums2) is odd.
3.XOR all elements of nums2 if len(nums1) is odd.
4.Return result..
'''

from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the result to 0 (XOR with 0 gives the number itself).
        result = 0        
        # XOR all numbers from nums1 if nums2 has an odd length
        if len(nums2) % 2 == 1:
            for num in nums1:
                result = result ^ num      
        # XOR all numbers from nums2 if nums1 has an odd length
        if len(nums1) % 2 == 1:
            for num in nums2:
                result = result ^ num             
        return result

nums1 = [2,1,3]
nums2 = [10,2,5,0]
print(Solution().xorAllNums(nums1, nums2))



