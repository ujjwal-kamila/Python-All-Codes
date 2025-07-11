# check if a number is palindrome or not
def check_palindrome(n):
    num = n
    res = 0 
    while num > 0 :
        last_dig = num % 10
        res = (res*10)+ last_dig
        num = num //10
    if n == res:
        return "Input is Palindome number "
    else:
        return "Not a Palindrome Number "
ans = check_palindrome(1221)
ans = check_palindrome(1234)
print(ans)