# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31 - 1
        neg = x < 0
        x = abs(x)
        str_x = str(x)
        
        # reverse
        rev_num = int(str_x[::-1])
        if neg:
            rev_num = -rev_num
        # for contraints 
        if rev_num < int_min or rev_num > int_max:
            return 0
        return rev_num

ans  = Solution().reverse(-123456)
ans  = Solution().reverse(1534236469)
print(ans)


''' Another method : not optimised'''

class Solution:
    def reverse(self, x: int) -> int:
        int_min, int_max = -2**31, 2**31 - 1
        neg = x < 0
        x = abs(x)
        rev_num = 0 
        
        while x>0:
            last_dig = x %10
            rev_num = rev_num * 10 + last_dig
            x//=10
        if neg:
            return -rev_num
        # for contraints 
        if rev_num < int_min or rev_num > int_max:
            return 0
        return rev_num
        
                

ans  = Solution().reverse(-123456)
ans  = Solution().reverse(1534236469)

print(ans)