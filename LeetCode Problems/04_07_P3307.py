# 3307. Find the K-th Character in String Game II
from typing import List
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        cnt = 0
        n = len(operations) - 1
        length = pow(2, n)

        for i in range(n, -1, -1):
            if length < k:
                k -= length
                if operations[i] == 1:
                    cnt += 1
            length //= 2

        return chr(ord('a') + (cnt % 26))
        

sol = Solution()
res =sol.kthCharacter(10,[0,1,0,1])
print("Output is :",res)