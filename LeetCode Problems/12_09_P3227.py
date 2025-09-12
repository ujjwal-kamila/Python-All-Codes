# 3227 Vowel game in a str

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        # If no vowels -> Alice cannot play -> Bob wins
        for ch in s:
            if ch in vowels:
                return True
        return False


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v=['a','e','i','o','u']
        for ch in s:
            if ch.lower() in v:
                return True
        return False


s = "leetcoder"
s = "bbcd"
ans = Solution().doesAliceWin(s)
print(ans)
