# 342. Power of Four

'''
Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false
'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

ans = Solution().isPowerOfFour(1)
print(ans)