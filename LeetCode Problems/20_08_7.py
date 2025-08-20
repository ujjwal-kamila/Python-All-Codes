# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        str_x = str(x)
        
        # reverse
        rev_num = int(str_x[::-1])
        if neg:
            rev_num = -rev_num
        return rev_num

ans  = Solution().reverse(-123456)
print(ans)


''' Another method '''

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x = abs(x)
        rev_num = 0 
        
        while x>0:
            last_dig = x %10
            rev_num = rev_num * 10 + last_dig
            x//=10
        if neg:
            return -rev_num
        return rev_num
        
                

ans  = Solution().reverse(-123456)
print(ans)