# Check if a String is Palindrome or Not 

'''
Original = Reverse = True
nitin -> nitin
'''
# using Recursion : better approach
class Solution:
    def helper(self, s, left, right):
        if left >= right:        
            return True
        if s[left] != s[right]:  # mismatch
            return False
        # move both pointers
        return self.helper(s, left + 1, right - 1)

    def isPalindrome(self, s: str) -> bool:
        # check the whole string
        return self.helper(s, 0, len(s) - 1)

print(Solution().isPalindrome("NITIN"))   
print(Solution().isPalindrome("LEVEL"))


print()

#  Iterative Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] != s[right]:   
                return False
            left += 1                
            right -= 1
        return True                   # all pairs matched

res = Solution().isPalindrome("NITIN")
print(res)














# using loop 
s = "NITIN"
left = 0
right = len(s) - 1
is_palindrome = True 

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)

# another method
s = "ABCD"
res = ""

for char in s:
    res = char + res  
print(res)
if s == res:
    print(True)
else:
    print(False)

