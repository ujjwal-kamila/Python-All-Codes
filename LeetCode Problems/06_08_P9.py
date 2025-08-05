# 9. Palindrome Number
'''
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num =x 
        res = 0
        while num>0:
            last_dig = num %10
            res = (res*10)+last_dig
            num = num //10
        return x==res

res = Solution().isPalindrome(121)
print(res)