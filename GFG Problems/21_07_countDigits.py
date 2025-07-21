# Count Digits

class Solution:
    def evenlyDivides(self,n):
        num =n
        count =0
        while num > 0:
            last = num%10
            count+=1
            num = num//10
        return count

res =Solution().evenlyDivides(12)
print(res)