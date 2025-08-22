# 344. Reverse String
from types import list
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap
            left += 1
            right -= 1


s = ["h","e","l","l","o"]
Solution().reverseString(s)
print(s)   # ["o","l","l","e","h"]
