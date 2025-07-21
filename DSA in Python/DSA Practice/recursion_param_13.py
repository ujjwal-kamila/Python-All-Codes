# Recursion using paramters
# print 'x'  n times

def func(x,n):
    if n == 0:
        return "finished"
    
    print(x)
    func(x,n-1)

func("ujjwal",5)

