#!/usr/bin/python

class Matrixes:
    def __init__(self, m):
        self.m = m

A = [(5,4),(4,6),(6,2),(2,7)]
storedDP = []
def DP(i,j):
    if (i,j) in storedDP:
        return storedDP[(i,j)]
    if i == j:
        return 0 
    elif i > j:
        return -1 # error
    else:
        temDP = []
        for k in range(i, j):
            temDP.append(DP(i,k) + DP(k+1,j) + A[i][0]*A[k][1]*A[j][1])
        storedDP[(i,j)] = min(temDP)
        return storedDP

print "DP(0,2) = ", DP(0,2)
print "DP(0,3) = ", DP(0,3)
