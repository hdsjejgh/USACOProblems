import sys
sys.stdin = open("time.in",'r')
sys.stdout = open("time.out",'w')

from collections import defaultdict



N,M,C = map(int,input().split())
payments = list(map(int,input().split()))
paths = defaultdict(list)
for i in range(M):
    a,b = map(int,input().split())
    paths[a-1].append(b-1)
best = [[-1]*N for i in range(1000)]
best[0][0]=0
res = -1
for t in range(1000):
    for n in range(N):
        if best[t][n]==-1:
            continue
        if t<999:
            for nn in paths[n]:
                best[t+1][nn] = max(best[t+1][nn], best[t][n] + payments[nn])
    res = max(res,best[t][0]-C*t**2)
print(res)