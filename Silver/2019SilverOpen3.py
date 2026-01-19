import sys
sys.stdin  = open("fenceplan.in", "r")
sys.stdout = open("fenceplan.out","w")

from collections import defaultdict

N, M = map(int,input().split())
cows = []
for i in range(N): cows.append(list(map(int,input().split())))
graph = defaultdict(list)
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

best = float('inf')
explored = [0]*N
groups = []

for i in range(1,N+1):
    if explored[i-1]==2: continue
    queue = [i]

    minx,miny = float('inf'), float('inf')
    maxx,maxy = 0,0
    while queue:
        item = queue.pop()

        x,y = cows[item-1]
        minx = min(x,minx)
        miny = min(y,miny)
        maxx = max(x,maxx)
        maxy = max(y,maxy)

        explored[item-1] = 2

        conn = graph[item]
        for c in conn:
            if explored[c-1]==0:
                queue.append(c)
                explored[c-1]=1
    perim = 2*(maxx-minx + maxy-miny)
    best = min(best,perim)


print(best)