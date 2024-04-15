def primeNumber(n):
    flag=False
    for i in range(2,n+1//2):
        if n%i==0:
            flag=True
            break

    if not flag:
        return True
    
n=int(input("Enter upto how much number you want to count: "))
def compute(n):
    sum=0
    for i in range(2,n):
        if primeNumber(i):
            sum+=i

    return sum

import eulerlib

print(sum(eulerlib.primes_wheel_fact(10)))
