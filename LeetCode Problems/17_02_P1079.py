# 1079. Letter Tile Possibilities
'''
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
'''




from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        
        # Generate all permutations for different lengths
        for length in range(1, len(tiles) + 1):
            sequences.update(permutations(tiles, length))
        
        return len(sequences)

# Test cases 
sol = Solution()
print(sol.numTilePossibilities("AAB")) 
print(sol.numTilePossibilities("AAABBC"))  
print(sol.numTilePossibilities("V"))