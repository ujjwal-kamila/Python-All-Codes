# 2264. Largest 3-Same-Digit Number in String

'''
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
'''
'''
Approach:
1.Loop through the string checking each substring of length 3.
2.If all digits in the substring are identical, compare it with the current maximum and update if larger.
3.Return the largest such substring found.
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-2):
            if num[i] ==num[i+1] == num[i+2]:
                ans = max(ans, num[i:i+2])
        return ans 
    
print(Solution().largestGoodInteger("6777133339"))  
print(Solution().largestGoodInteger("2300019"))   
print(Solution().largestGoodInteger("42352338"))  
