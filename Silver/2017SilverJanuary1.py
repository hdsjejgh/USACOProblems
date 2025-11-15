import sys
sys.stdin = open("cowdance.in","r")
sys.stdout = open("cowdance.out","w")

import heapq
from bisect import bisect_left
N,Tm = map(int,input().split())
cows = []
for i in range(N):
    cows.append(int(input()))


l=1
r=N
while l<=r:
    m=l+(r-l)//2

    p = cows[:m]
    heapq.heapify(p)
    for i in range(m, N):
        exit_time = heapq.heappop(p) + cows[i]
        heapq.heappush(p, exit_time)
    if max(p)>Tm:
        l=m+1
    else:
        r=m-1
print(l)