#!/usr/bin/python
import time as time
# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

def count(S, m, n):
    """
    S is a list of coins
    m is the number of element within S considering
    n is the money
    """
    # if n is 0, there is 1 solution
    if n == 0: return 1
    if n < 0: return 0
    if m <= 0 and n >= 1: return 0
    return (count(S, m-1, n) + count(S, m, n-S[m-1]))

memo = {}
def count1(S, m, n):
    """
    apply memoize 
    """
    if (m,n) in memo:
        return memo[(m,n)]
    if n == 0: f = 1
    if n < 0: f = 0
    if m <= 0 and n >= 1: f = 0
    f = count(S, m - 1, n) + count(S, m, n-S[m-1])
    memo[(m,n)] = f
    return f
      
def count2(S,m,n):
    """
    Bottom-up topological order
    """
    memo = [[0 for x in range(m)] for x in range(n+1)]
    for i in range(m):
        memo[0][i] = 1
    for i in range(1, n+1):
        for j in range(m):
            x = memo[i-S[j]][j] if i - S[j] >=0 else 0
            y = memo[i][j-1] if j >=1 else 0
            memo[i][j] = x + y
    return memo[n][m-1]

def count3(S,m,n):
    """
    Bottom-up topological order
    """
    memo = {} 
    for i in range(m):
        memo[(i,0)] = 1
    for j in range(1,n+1):
        memo[(0,j)] = 0
    for i in range(1, n+1):
        for j in range(m):
            x = memo[(j,i-S[j])] if i - S[j] >=0 else 0
            y = memo[(j-1, i)] if j >=1 else 0
            memo[(j,i)] = x + y
    return memo[(m-1,n)]

S = [10, 20, 50, 100]
print "DP(30) = ", count(S,len(S), 30)
print "DP(50) = ", count(S,len(S), 50)
print "DP1(50) = ", count1(S,len(S), 50)
print "DP2(50) = ", count2(S,4, 50)
print "DP(150) = ", count(S,4, 150)
print "DP1(150) = ", count1(S,4, 150)
print "DP2(150) = ", count2(S,4, 150)
print "DP3(150) = ", count3(S,len(S), 150)
s = time.time()
print "count(1000) = ", count(S,4, 1000)
print "spent ", time.time() - s
s = time.time()
print "count1(1000) = ", count1(S,4, 1000)
print "spent ", time.time() - s
s = time.time()
print "count2(1000) = ", count2(S,4, 1000)
print "spent ", time.time() - s
s = time.time()
print "count3(1000) = ", count3(S,4, 1000)
print "spent ", time.time() - s
