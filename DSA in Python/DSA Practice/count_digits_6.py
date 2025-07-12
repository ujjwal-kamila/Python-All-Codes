# count how many digits 
n = 5110
def count_digits(n):
    num = n 
    count = 0 

    while num > 0:
        count += 1
        num = num //10
    return count

res = count_digits(5110)
print(res)



# using log base 
from math import * 
def count_digit(num):
    return int(log10(num)+1)

res = count_digit(5438128)
print(res)

