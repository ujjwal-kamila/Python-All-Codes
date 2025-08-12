# 13. Roman to Integer

'''
Input: s = "III"
Output: 3
Explanation: III = 3.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_val = 0
        # Loop from last to first
        for char in reversed(s):
            val = roman_map[char]
            if val < prev_val:
                total = total-val
            else:
                total = total +val
            prev_val = val
        return total
    

print(Solution().romanToInt("III"))   
print(Solution().romanToInt("LVIII")) 
print(Solution().romanToInt("MCMXCIV"))