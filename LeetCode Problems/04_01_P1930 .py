# 1930. Unique Length-3 Palindromic Subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)  # filter out duplicate characters
        res = 0

        # Iterate through each unique letter
        for letter in letters:
        # Find the first and last occurrence of the character
            leftIndex = s.index(letter)  # 1st occurrence
            rightIndex = s.rindex(letter)  #last occurrence

            #Ensure that there is a substring between the first and last occurrence
            if rightIndex > leftIndex + 1:
                #Get unique characters in the substring that lies between left and right occurrences
                newSet = set(s[leftIndex + 1: rightIndex])

                #Add the length of unique characters in the middle part
                res += len(newSet)

        return res

# Test case
s = "adc"
solution = Solution()
print(solution.countPalindromicSubsequence(s))


