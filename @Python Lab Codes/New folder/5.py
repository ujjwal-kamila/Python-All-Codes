def gcd(a,b):
    if b==0:
        return abs(a)
    else:
        return gcd(b,a%b)
    
def lcm(a,b):
    return (a*b)//gcd(a,b)
    
def computeUpto(n):
    ans=1
    for i in range(1,n+1):
        ans*=i//gcd(i,ans)
    return ans

n=int(input("Enter the Number: "))
print(computeUpto(n))
print(lcm(60,48))