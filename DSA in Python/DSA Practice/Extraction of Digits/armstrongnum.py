# check if a number is armstrong number or not 

def check_armstrong(n):
    num = n
    total = 0
    num_of_dig = len(str(num))
    while num > 0:
        ld = num % 10
        total = total + (ld ** num_of_dig)
        num = num // 10
    if total == n:
        return "The input number is Armstrong number!"
    else:
        return "Not a Armstong number!"
    
res = check_armstrong(153)
res = check_armstrong(9474)
print(res)