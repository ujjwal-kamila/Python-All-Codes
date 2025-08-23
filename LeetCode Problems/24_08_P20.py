# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in map: # if closing bracket
                if stack and stack[-1] == map[ch]:
                    stack.pop()
                else:
                    return False
            else:  # if opening bracket
                stack.append(ch)
        
        return not stack

# test cases
print(Solution().isValid("()"))       
print(Solution().isValid("()[]{}"))   