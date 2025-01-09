# 2185. Counting Words With a Given Prefix


# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

''' 
Explanation:
We need to count the words in the list that start with a given prefix. 
..
The prefix matching can be efficiently done using the built-in startswith() method.
'''

# Approach:
# 1.Loop through words: Go through each word in the list.
# 2.Check prefix: Use startswith(pref) to see if the word starts with the prefix.
# 3.Count matches: Increase the count for matching words.
# 4.Return the count: Finally, return the total count of matches.


from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0  # Initialize the counter
        for word in words:
            # Check if the word starts with the prefix
            if word.startswith(pref):
                count += 1
        return count

# Test cases
sol = Solution()

# Example 1
words1 = ["pay", "attention", "practice", "attend"]
pref1 = "at"
print(sol.prefixCount(words1, pref1))  # Output: 2

# Example 2
words2 = ["leetcode", "win", "loops", "success"]
pref2 = "code"
print(sol.prefixCount(words2, pref2))  # Output: 0
