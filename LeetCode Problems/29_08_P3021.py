# 3021 :leetcode probelm Alice and bob playing game 


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count of odd and even numbers from 1 to n
        odd_x = (n + 1) // 2  
        even_x = n // 2        

        # Count of odd and even numbers from 1 to m
        odd_y = (m + 1) // 2  
        even_y = m // 2     
        # total valid pairs = (odd_x * even_y) + (even_x * odd_y)
        result = odd_x * even_y + even_x * odd_y  

        return result
        # OR simply: return (n * m) // 2


sol = Solution()
print(sol.flowerGame(3, 4))  
print(sol.flowerGame(2, 2))  
print(sol.flowerGame(5, 5))  
