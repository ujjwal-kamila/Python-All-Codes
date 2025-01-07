# 1408. String Matching in an Array

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]

''' Explanation:
The word "as" is a substring of "mass", and "hero" is a substring of "superhero".
Calculate all words that are substrings of other words in the list.
'''

# Approach:# Use nested loops to check substrings for every pair of words, ensuring the word is not compared with itself.

from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Initialize a set to store unique substrings
        substrings = set()
        
        # Iterate through every pair of words to check for substrings
        for i in range(len(words)):
            for j in range(len(words)):
                # Ensure the word is not compared with itself
                if i != j and words[i] in words[j]:
                    substrings.add(words[i])
        
        # Convert set to list and return the result
        return list(substrings)

# Test cases
sol = Solution()

# Test case 1
words1 = ["mass", "as", "hero", "superhero"]
print(sol.stringMatching(words1))  # ["as", "hero"]

# Test case 2
words2 = ["leetcode", "et", "code"]
print(sol.stringMatching(words2))  # ["et", "code"]

# Test case 3
words3 = ["blue", "green", "bu"]
print(sol.stringMatching(words3))  # []
