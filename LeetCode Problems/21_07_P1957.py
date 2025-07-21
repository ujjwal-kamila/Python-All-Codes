# 1957. Delete Characters to Make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                count =1
            
            if count<3:
                res += s[i]
            
        return s[0]+res
    
sol = Solution()
res =sol.makeFancyString("aaabaaaa")
print(res)