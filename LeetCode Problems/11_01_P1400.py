# 1400. Construct K Palindrome Strings
#source: https://leetcode.com/problems/construct-k-palindrome-strings/

''' 
Explanation:
We need to determine if it is possible to construct k 
palindrome strings using all characters in s.
To do this, count how many characters have odd frequencies since a palindrome can only have at most one odd-frequency character.
'''

'''
Approach:
1.Count the frequency of each character in s.
2.Count how many characters have odd frequencies.
3.If >len(s), return False (not enough characters for k palindromes).
4.Return True if the odd-frequency count is less than or equal to k, otherwise return False.'''


from collections import Counter

class Solution:
    def canConstruct(self, s, k):
        # If k > length of s, return False
        if k > len(s):
            return False
        
        # Count frequencies of characters in s
        char_count = Counter(s)
        
        # Count characters with odd frequencies
        odd_count = sum(freq % 2 for freq in char_count.values())
        
        # To form k palindromes, odd_count must be <= k
        return odd_count <= k

# Test Cases
solution = Solution()
print(solution.canConstruct("annabelle", 2))  # True
print(solution.canConstruct("leetcode", 3))  # False
