#!/usr/bin/python


def fib0(n):
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    memo[n] = f
    return f

def fib2(n):
    """
    using bottom-up topological order
    """
    fib = {}
    for i in range(1, n+1):
        if i <= 2:
            f = 1
        else:
            f = fib[i-1] + fib[i-2]
        fib[i] = f
    return fib[n]

print fib(8)
print "fib(100) = ", fib(100) 
print "fib2(100) = ", fib2(100) 
