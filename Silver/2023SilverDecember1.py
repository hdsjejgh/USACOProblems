from bisect import insort
from collections import deque

N,M,K = map(int,input().split())
counts = {}
weights = []
for i in range(N):
    value,amount = map(int,input().split())
    counts[value]=amount
    insort(weights,value)

weights = weights[::-1]

towers = deque([[1e100,M]])

ans = 0
for w in weights:
    amount = counts[w]
    remain = amount
    while len(towers)>0 and remain>0 and w+K<=towers[0][0]:
        if towers[0][1] > remain:
            towers[0][1]-=remain
            remain=0
        else:
            remain-=towers[0][1]
            towers.popleft()
    count = amount-remain
    if count>0:
        towers.append([w,count])
        ans+=count

print(ans)