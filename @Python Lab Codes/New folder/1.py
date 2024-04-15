def sumOfMultiples(N):
    """
    The function calculates the sum of all multiples of 3 or 5 up to a given number N.
    
    :param N: The function `sumOfMultiples(N)` calculates the sum of all multiples of 3 or 5 up to the
    number `N`. In this case, the function is called with `N` set to 1000, so it will calculate the sum
    of all multiples of 3 or
    :return: The function `sumOfMultiples(N)` calculates the sum of all multiples of 3 or 5 up to the
    number `N`. In this specific case, the function is called with `N` set to 1000. The function
    calculates the sum of all multiples of 3 or 5 up to 1000 and returns this sum. The returned value
    will be the sum of all
    """
    # The line `sum=0` initializes a variable `sum` to 0. This variable will be used to store the sum
    # of all the multiples of 3 or 5.
    sum=0
    for i in range(N):
        # The line `if i%3==0 or i%5==0:` checks if the current number `i` is divisible by either 3 or
        # 5. If it is, then the number is a multiple of either 3 or 5.
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum

print(sumOfMultiples(1000))
