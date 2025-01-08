# 3042. Count Prefix and Suffix Pairs I

# Input: words = ["a", "aba", "ababa", "aa"]
# Output: 4

''' 
Explanation:
The word "a" is a prefix and suffix of "aba", "ababa", and "aa". 
Also, the word "aba" is a prefix and suffix of "ababa".
'''

# Approach: Use nested loops to check if words[i] is a prefix and suffix of words[j] (i < j).
# Use the `startswith` and `endswith` string methods to perform the checks.

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0  # count valid pairs
        for i in range(len(words)):
            for j in range(len(words)):
                # Only consider pairs where i < j
                if i < j:
                    # Check if words[i] is both a prefix and suffix of words[j]
                    if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                        count += 1  # Increment the count if met the condition
        return count

# Test cases
sol = Solution()

# Test case 1
words1 = ["a", "aba", "ababa", "aa"]
print(sol.countPrefixSuffixPairs(words1))  # Output: 4

# Test case 2
words2 = ["pa", "papa", "ma", "mama"]
print(sol.countPrefixSuffixPairs(words2))  # Output: 2

# Test case 3
words3 = ["abab", "ab"]
print(sol.countPrefixSuffixPairs(words3))  # Output: 0
