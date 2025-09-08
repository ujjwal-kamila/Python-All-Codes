# 1317. Convert Integer to the Sum of Two No-Zero Integers


class Solution:
    def getNoZeroIntegers(self, n: int):
        for a in range(1, n):
            b = n - a
            print(a)
            print(b)
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]

# test cases
sol = Solution()
ans = sol.getNoZeroIntegers(11)
print(ans)