def primeNumber(n):
    flag=False
    for i in range(2,n//2):
        if n%i==0:
            flag=True
            break
    
    if not flag:
        return True
    else:
        return False
    
def highestPrimeFactor(num):
    highest=0
    # The code is iterating through numbers from 2 to `num//2` (integer division) using the `for`
    # loop. For each number `i`, it checks if `num` is divisible by `i` (`num % i == 0`), if `i` is a
    # prime number (using the `primeNumber` function), and if `i` is greater than or equal to the
    # current highest prime factor (`i >= highest`).
    for i in range (2,num//2):
        if num%i==0 and primeNumber(i) and i>=highest:
            highest=i
    print(highest)

print(primeNumber(5))