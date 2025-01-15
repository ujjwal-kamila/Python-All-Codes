# 2429. Minimize XOR
# Input: num1 = 3, num2 = 5
# Output: 3
# Explanation:
# The binary representations of num1 and num2 are 0011 and 0101, respectively.
# The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.


'''
Explanation:
We need to modify num1 so that it has the same number of set bits (1's) as num2, 
while minimizing the XOR result between num1 and the modified number.
The XOR is minimized when the binary representations of both numbers have more overlap.
'''

'''
Approach:
1. Count the number of set bits in num2.
2. Count the number of set bits in num1.
3. If num1 has more set bits than num2, remove extra bits from num1.
4. If num1 has fewer set bits than num2, add missing set bits to num1.
5. Return the modified num1 that minimizes the XOR result with num2.
'''

class Solution:
    def minimizeXor(self, num1, num2):
        # Count the set bits of num1 and num2
        set_bits_num1 = bin(num1).count('1')
        set_bits_num2 = bin(num2).count('1')
        
        # Initialize result as num1
        res = num1
        
        # Start by ensuring the number of set bits in res equals set_bits_num2
        if set_bits_num1 < set_bits_num2:
            # Add more set bits (1's) to result from least significant positions
            for i in range(32):
                if (res & (1 << i)) == 0 and set_bits_num1 < set_bits_num2:
                    res |= (1 << i)
                    set_bits_num1 += 1
        elif set_bits_num1 > set_bits_num2:
            # Remove some set bits (turn off 1's) from result
            for i in range(32):
                if (res & (1 << i)) != 0 and set_bits_num1 > set_bits_num2:
                    res &= ~(1 << i)
                    set_bits_num1 -= 1
        
        return res

# Test Cases
solution = Solution()
print(solution.minimizeXor(3, 5))  # Output: 3
print(solution.minimizeXor(1, 12))  # Output: 3
