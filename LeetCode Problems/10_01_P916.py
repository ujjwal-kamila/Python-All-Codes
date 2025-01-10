# 916. Word Subsets

#  find all strings in words1 that contain every character in each string from words2 with at least the required frequency.

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]

''' 
Explanation:
We need to find words in words1 where every string in words2 is a subset of the word.
This means each word in words1 must contain all characters in words2 with at least the required frequencies.
We can efficiently check this using Counter and comparing character frequencies.
'''

# Approach:
# 1. Calculate the maximum character count needed from words2.
# 2.Check each word in words1 to ensure it satisfies the character requirements from words2.
# 3.Collect and return all valid words that meet the criteria.

from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        # Step 1: Compute the aggregate requirement for words2
        max_counts = Counter()
        for word in words2:
            for char, count in Counter(word).items():
                max_counts[char] = max(max_counts[char], count)

        # Step 2: Check each word in words1 against the aggregate requirement
        result = []
        for word in words1:
            word_count = Counter(word)
            # Check if all characters in max_counts are satisfied in word_count
            if all(word_count[char] >= count for char, count in max_counts.items()):
                result.append(word)

        return result
    
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]
solution = Solution()
print(solution.wordSubsets(words1, words2))
