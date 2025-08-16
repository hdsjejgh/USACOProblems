import sys
sys.stdin = open("socdist.in",'r')
sys.stdout = open("socdist.out",'w')

from bisect import bisect_left

N,M = map(int,input().split())
intervals = []
for i in range(M):
    intervals.append(list(map(int,input().split())))
intervals.sort()

def canplace(d):
    cows = N
    prev = intervals[0][0] - d
    for begin, end in intervals:
        if prev+d<begin: 
            prev = begin-d
        while begin <= prev + d <= end:
            prev += d
            cows -= 1
    return cows <= 0

l=0; r=intervals[-1][1] - intervals[0][0]
while l<r:
    m=(l+r+1)//2
    if canplace(m):
        l = m
    else:
        r = m - 1
print(l)