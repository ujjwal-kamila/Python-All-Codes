def factors(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    
    return count

def triangleNumber(terms):
    sum=0
    for i in range(1,terms+1):
        sum+=i
    
    return sum

def compute():
    num=0
    count=num+1
    while factors(num) < 6:
        num+=count

    return num

print(compute())
