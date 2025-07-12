# print all the factors of a given num 

# Brute force approach 
def find_factors(n):
    num = n
    res = []
    for i in range (1, num+1):
        if num % i == 0 :
            res.append(i)
    return res

res = find_factors(10)
print(res)


# Better Solution 
def find_factor(n):
    num = n 
    res = []
    for i in range(1, num +1 //2):
        if num % i == 0:
            res.append(i)
    res.append(num)
    return res

ans = find_factor(20)
print(ans)



# optimal solution 
from math import sqrt
def find_factor(n):
    num = n 
    res = []
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            res.append(i)
            if num//i != i:
                res.append(num//i)
    res.sort()
    return res

ans = find_factor(20)
print(ans)
