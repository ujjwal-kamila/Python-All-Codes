# 1323. Maximum 69 Number
'''
changes only the first '6' to '9'
'''

'''
Input: num = 9669
Output: 9969

Input: num = 9996
Output: 9999
'''
'''
Apprach:
1.Make the list of str from int
2.Replace the first '6' with '9' to maximize the number
3.convert the str to int 
'''

class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = list(str(num))
        
        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break
        
        return int("".join(num_str))
        # return int(str(num).replace('6', '9', 1))


# test cases
obj = Solution()
print(obj.maximum69Number(9669)) 
print(obj.maximum69Number(9996))  
print(obj.maximum69Number(9999))
