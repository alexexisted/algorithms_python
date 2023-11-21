def factorial(n):
    if n == 0:  #if n is 0, return 1
        return 1
    return n * factorial(n-1)   #while n id greater than 0, recursion will run


print(factorial(6))


