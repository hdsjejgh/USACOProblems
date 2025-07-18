import sys
sys.stdin = open("pails.in",'r')
sys.stdout = open("pails.out",'w')

from collections import deque

X,Y,K,M = map(int,input().split())
grid = [[0 for i in range(Y+1)] for i in range(X+1)]
optimum = float('inf')


q = deque([(0,0,0)])
while q:
    state = q.popleft()
    k,x,y = state
    grid[x][y]=1
    optimum = min(abs(M-(x+y)),optimum)

    if k == K:
        continue
    
    #empty
    if x!=0:
        s = (k+1,0,y)
        if not grid[s[1]][s[2]]:
            q.append(s)
    if y!=0:
        s = (k+1,x,0)
        if not grid[s[1]][s[2]]:
            q.append(s)
    
    #fill
    if x!=X:
        s = (k+1,X,y)
        if not grid[s[1]][s[2]]:
            q.append(s)
    if y!=Y:
        s = (k+1,x,Y)
        if not grid[s[1]][s[2]]:
            q.append(s)

    #pour
    yemp,xemp = Y-y,X-x
    if yemp>=x and yemp!=0:
        s = (k+1,0,y+x)
        if not grid[s[1]][s[2]]:
            q.append(s)
    if xemp>=y and xemp!=0:
        s = (k+1,x+y,0)
        if not grid[s[1]][s[2]]:
            q.append(s)
    if yemp<x:
        s = (k+1,x-yemp,Y)
        if not grid[s[1]][s[2]]:
            q.append(s)
    if xemp<y:
        s = (k+1,X,y-xemp)
        if not grid[s[1]][s[2]]:
            q.append(s)


print(optimum)