# Extract digits using loops 
n = 5875
num = n
print("All Digits are : ")
while num > 0 :
    last = num % 10
    print(last)
    num = num//10