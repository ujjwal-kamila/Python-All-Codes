# Find the Fibonacci Number
# Leetcode : 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n ==1 :
            return n
        return self.fib(n-1)+self.fib(n-2)

ans = Solution().fib(5)
print(ans)

# or can do using 

class Solution:
    def fun(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fun(n-1) + self.fun(n-2)

    def fib(self, n: int) -> int:
        return self.fun(n)


print(Solution().fib(5))  
