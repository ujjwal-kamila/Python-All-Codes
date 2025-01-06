# 1769. Minimum Number of Operations to Move All Balls to Each Box

# Input: boxes = "110"
# Output: [1,1,3] 
'''
Explantion: I have 3 boxes b1 b2 b3 ,
b1,b2 have 1 balls 
b3 empty

calculate total pass to move all balls to each box as [b1 pass ,b2pass ,b3pass]'''

# Approach:Two passes (left-to-right, right-to-left) accumulate ball movements, reducing time complexity to O(n)

from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        # 1st pass Left to right pass: Count balls and moves
        balls = 0
        moves = 0
        for i in range(n):
            result[i] += moves
            balls += int(boxes[i])  # Add ball count
            moves += balls  # Increment moves for next position

        # 2nd pass Right to left pass: Update moves for right side
        balls = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            result[i] += moves
            balls += int(boxes[i])  # Add ball count
            moves += balls  # Increment moves for next position
        
        return result

# Test case
sol = Solution()
print(sol.minOperations("110"))  # [1,1,3]


    