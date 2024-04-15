def is_prime(n):
    flag=False
    for i in range(2,n//2):
        if n%i==0:
            flag=True
            break
    
    if not flag:
        return True

def nth_prime(n):
    count = 0
    number = 2
    while count < n:
        if is_prime(number):
            count += 1
        number += 1
    return number - 1

n=int(input("Enter any Number : "))
print(str(nth_prime(n)))