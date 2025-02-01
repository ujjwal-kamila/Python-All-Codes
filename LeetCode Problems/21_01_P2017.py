# 2017. Grid Game



# Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
# Output: 2
'''

'''

# Explanation:
# Given a matrix and an array of numbers, paint the cells according to the 
# numbers in the array. The goal is to return the smallest index at which 
# either a row or column gets completely painted.

'''
Approach:
1. Create a dictionary to store the position of each number in the matrix.
2. Use two arrays to track the count of painted cells for each row and column.
3. For each number in the array, find its position in the matrix and increment 
   the row and column counters.
4. Check if any row or column is fully painted.
5. If any row or column is painted, return the current index from the array.
'''

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # Step 1: Create a map to store the position of each element in the matrix mat
        positions = {}
        for r in range(m):
            for c in range(n):
                positions[mat[r][c]] = (r, c)
        
        # Step 2: Arrays to track number of painted cells per row and column
        row_paint_count = [0] * m
        col_paint_count = [0] * n
        
        # Step 3: Paint the cells based on arr
        for i in range(len(arr)):
            num = arr[i]
            row, col = positions[num]
            
            # Paint the cell
            row_paint_count[row] += 1
            col_paint_count[col] += 1
            
            # Step 4: Check if any row or column is fully painted
            if row_paint_count[row] == n or col_paint_count[col] == m:
                return i
        
        return -1  # In case no row or column gets fully painted.

# Test cases
arr1 = [1, 3, 4, 2]
mat1 = [[1, 4], [2, 3]]
print(Solution().firstCompleteIndex(arr1, mat1))  # Output: 2

arr2 = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat2 = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
print(Solution().firstCompleteIndex(arr2, mat2))  # Output: 3
