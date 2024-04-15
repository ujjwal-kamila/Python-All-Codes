def compute():
    n=1000
    for a in range(1,n+1):
        for b in range(a+1,n+1):
            c=n-a-b
            if c*c == a*a + b*b:
                return str(a*b*c)

print(compute())
