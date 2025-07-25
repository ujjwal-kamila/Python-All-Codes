# Functional recursion means return something 
'''
1. create flow
2. create base condition
'''

# examples

# sum of 1 to n paramterised way 
def print_sum(sum,i,n):
    if i>n:
        print(sum)
        return
    return print_sum(sum+i,i+1,n)

res = print_sum(0,1,4)


# another example
def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

# sum from 1 to 5
x = find_sum(5)
print(x)