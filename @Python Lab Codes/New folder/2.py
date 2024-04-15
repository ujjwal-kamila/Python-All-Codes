def evenFibonacciSum(terms):
    # The code initializes three variables: `a` is set to 0, `b` is set to 1, and `sum` is set to 0.
    a=0
    b=1
    sum=0
    # The code block `for i in range(terms):` is a loop that iterates `terms` number of times.
    for i in range(terms):
        # In the line `a,b=b,a+b`, the values of `a` and `b` are being swapped.
        a,b=b,a+b
        # The code `if b%2==0:` checks if the current Fibonacci number `b` is divisible by 2, which
        # means it is an even number. If `b` is indeed even, then `sum=sum+b` adds the value of `b` to
        # the variable `sum`. This is done to calculate the sum of all the even Fibonacci numbers
        # encountered so far.
        if b%2==0:
            sum=sum+b
    print(sum)
    
evenFibonacciSum(10)