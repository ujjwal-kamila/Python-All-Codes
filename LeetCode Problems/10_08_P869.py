# 869. Reordered Power of 2
''' Return true if and only if we can do this so that the resulting number is a power of two.......
Input: n = 1
Output: true
'''


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # check 2^0 to 2^30
        for i in range(31):
            if sorted(str(n))== sorted(str(2 ** i)):
                return True
        return False

res = Solution().reorderedPowerOf2(10)
print(res)


'''
Sort the digits of n.
Sort the digits of every power of two (from 2^0 to 2^30).
If any match, return True; else False.
'''