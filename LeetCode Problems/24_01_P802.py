# 802 Find Eventual Safe States

from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)  # Number of nodes
        status = [0] * n  # Track node states: 0 = unvisited, 1 = visiting, 2 = safe
        result = []

        def is_safe(node):
            # If the node is being visited, it means we found a cycle
            if status[node] == 1:
                return False
            # If the node is already marked as safe, return True
            if status[node] == 2:
                return True
            
            status[node] = 1  # Mark the node as being visited
            for neighbor in graph[node]:
                if not is_safe(neighbor):  # If any neighbor is not safe, this node is also not safe
                    return False
            
            status[node] = 2  # Mark the node as safe
            return True

        # Check every node
        for i in range(n):
            if is_safe(i):  # If the node is safe, add it to the result
                result.append(i)
        
        return result


graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
solution = Solution()
print(solution.eventualSafeNodes(graph))
graph = [[]]
print(Solution().eventualSafeNodes(graph))  

