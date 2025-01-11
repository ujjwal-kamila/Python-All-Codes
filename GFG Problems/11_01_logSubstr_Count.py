# Longest substring with distinct characters
#source = "https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1"
# Given a string s, find the length of the longest substring with all distinct characters. 
# Input: s = "geeksforgeeks"
# Output: 7
# Explanation: "eksforg" is the longest substring with all distinct characters.


class Solution:
    def longestUniqueSubstr(self, s):
        char_set = set()
        left = 0
        max_length = 0
    
        # Use a sliding window to traverse the string
        for right in range(len(s)):
            # If the current character is already in the set, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
    
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
    
        return max_length

solution = Solution()
print(solution.longestUniqueSubstr("geeksforgeeks"))  # Output: 7
print(solution.longestUniqueSubstr("aaa"))           # Output: 1
print(solution.longestUniqueSubstr("abcdefabcbb"))   # Output: 6
