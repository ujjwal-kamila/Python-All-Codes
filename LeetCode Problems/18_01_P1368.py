# 1368. Minimum Cost to Make at Least One Valid Path in a Grid

# Problem Overview:
# You are given a grid where each cell has an arrow directing to one of the four adjacent cells.
# Moving in the direction the arrow points doesn’t cost anything (0-cost), but if you change the direction to go to the next cell, it incurs a cost (1-cost).


# 0-1 BFS Approach: In this method.......Use BFS for grid traversal.
# Use a deque (double-ended queue) to process 0-cost movements first by adding them to the front and 1-cost movements to the back. This allows processing the grid with priority for cheaper paths.

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from collections import deque

class Solution:
    def minCost(self, grid):
        # Directions: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        
        numRows, numCols = len(grid), len(grid[0])  # Get grid dimensions      
        # Initialize minCost array with infinity
        minCost = [[float('inf')] * numCols for _ in range(numRows)]
        minCost[0][0] = 0  # Start at (0,0)
        
        # Deque for BFS
        dq = deque([(0, 0)])  # Queue starts at (0, 0)
        
        while dq:
            r, c = dq.popleft()  # Get current position            
            # Check all directions
            for i, (dr, dc) in enumerate(dirs):  
                nr, nc = r + dr, c + dc  # New position                
                # Check bounds
                if 0 <= nr < numRows and 0 <= nc < numCols:
                    # Calculate cost (0 if preferred, 1 if not)
                    cost = 0 if grid[r][c] == i + 1 else 1  
                    newCost = minCost[r][c] + cost  # New cost
                    
                    # Update if cheaper
                    if newCost < minCost[nr][nc]:
                        minCost[nr][nc] = newCost
                        if cost == 1:
                            dq.append((nr, nc))  # Add to back
                        else:
                            dq.appendleft((nr, nc))  # Add to front
        
        # Return the minimum cost to bottom-right
        return minCost[numRows - 1][numCols - 1]


sol = Solution()
print(sol.minCost([[1,1,1,1], [2,2,2,2], [1,1,1,1], [2,2,2,2]]))   # 3
print(sol.minCost([[1,1,3], [3,2,2], [1,1,4]]))  #  0
print(sol.minCost([[1,2], [4,3]]))  #  1
utput: 0
print(sol.minCost([[1,2], [4,3]]))  #  1