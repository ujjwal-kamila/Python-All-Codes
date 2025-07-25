# find factorial of an given number 
# n! = n * (n-1)!

# 1.using for loop
def factorial_for(n):
    res = 1
    for i in range (2,n+1):
        res = res*i
    return res

res = factorial_for(5)
print(res)


# 3.Using built in math 
import math
print(math.factorial(5)) 

# Better approach usig recursion :
def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)

print(factorial_rec(6))


# using parameterised recursion 
def factorial_param(n, result=1):
    if n == 0 or n == 1:
        return result
    return factorial_param(n - 1, result * n)

print(factorial_param(5))  
