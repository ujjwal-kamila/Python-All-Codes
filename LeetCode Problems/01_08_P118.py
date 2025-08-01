# 118. Pascal's Triangle
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]  
        
        for i in range(1, numRows):
            prev_row = res[-1]
            new_row = [1]
            
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])
                
            new_row.append(1)
            res.append(new_row)
        
        return res

res = Solution().generate(5)
print(res)