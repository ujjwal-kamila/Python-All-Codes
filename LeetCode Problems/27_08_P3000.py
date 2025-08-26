# Leetcode : 3000. Maximum Area of Longest Diagonal Rectangle

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = float("-inf")  # max diagonal squared
        max_area = float("-inf")  # store area 
        
        for l, w in dimensions:
            sq = l*l + w*w          
            area = l * w            

            if sq > max_diag:       
                max_diag = sq
                max_area = area
            elif sq == max_diag:  
                max_area = max(max_area, area)
                
        return max_area

# test cases
print(Solution().areaOfMaxDiagonal([[9,3],[8,6]]))
print(Solution().areaOfMaxDiagonal([[3,4],[4,3]]))
