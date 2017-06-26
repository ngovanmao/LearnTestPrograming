#!/usr/bin/python

S = [10, 20, 50, 100]
N = 100
combined = [[]]
failed = False
def DP(n):
    global failed 
    tempDP = []
    if n <= 0:
        return 0
    else:
        for i in range(len(S)):
           tempDP.append(1 + DP(n-S[i]))
        return S.index(min(tempDP)

N = DP(30) 
if failed:
    print "error"
else:
    print "DP(100) = ", N
