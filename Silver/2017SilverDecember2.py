import sys
sys.stdin = open("measurement.in","r")
sys.stdout = open("measurement.out","w")

import heapq
from collections import defaultdict
import bisect

N,G = map(int,input().split())
logs = []
for i in range(N): 
    logs.append(list(map(int,input().split())))
logs.sort()
change = 0

sorted_arr = []
cows = list(set(i[1] for i in logs))
values = {}
for c in cows:
    values[c] = G
    sorted_arr.append([G,c])

sorted_arr.append([G,float("inf")])
top_cows = sorted(set(cows + [float("inf")]))
for t,c,d in logs:
    index = bisect.bisect_left(sorted_arr, [values[c], c])
    sorted_arr.pop(index)
    values[c]+=d
    bisect.insort(sorted_arr,[values[c],c])
    
    highest = sorted_arr[-1][0]

    top_2 = []
    for value,cow in sorted_arr:
        if value==highest:
            top_2.append(cow)
    top_2.sort()
    if top_2!=top_cows:
        top_cows=top_2
        change+=1


print(change)