n=int(input("Enter a Number : "))
def diff(n):
    sum=0; squareSum=0; sumSquare=0
    for i in range(1,n+1):
        sum+=i
        squareSum=sum**2
        sumSquare+=i*i
    
    return squareSum - sumSquare

print(diff(n))