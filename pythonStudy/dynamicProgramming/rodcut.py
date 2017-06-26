#!/usr/bin/python
p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

def DP(n):
    r = {}
    r[0] = 0
    s = {} # size of piece to be taken out from rod j
    for j in range(1,n+1):
        q = -1000
        for i in range(1,j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    return r, s

rod, sz = DP(10)
print "rod, sz = ", rod, sz
