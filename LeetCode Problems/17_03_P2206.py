# 2206. Divide Array Into Equal Pairs

from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = Counter(nums)  # Count occurrences of each number
        
        # Check if all numbers have even occurrences
        for count in freq.values():
            if count % 2 != 0:
                return False
        
        return True

# Test cases
sol = Solution()
print(sol.divideArray([3, 2, 3, 2, 2, 2]))  
print(sol.divideArray([1, 2, 3, 4]))      
