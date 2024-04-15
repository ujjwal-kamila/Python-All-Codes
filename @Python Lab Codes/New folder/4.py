def palindrome(num):
    number=num
    reverse=0
    while num>0:
        l_digit=num%10
        reverse=reverse*10+l_digit
        num//=10

    return True if number==reverse else False

def highPalinProduct(power):
    for i in range(10**power-1,10**(power-1),-1):
        for j in range(10**power-1,10**(power-1),-1):
            if palindrome(i*j):
                return i*j

print(highPalinProduct(3))
