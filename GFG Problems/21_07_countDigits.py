# Count Digits

class Solution:
    def evenlyDivides(self,n):
        num =n
        while num > 0:
            last = num%10
            print(last)
            num = num//10

res =Solution().evenlyDivides(12)