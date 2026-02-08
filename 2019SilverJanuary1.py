import sys
sys.stdin = open("perimeter.in","r")
sys.stdout = open("perimeter.out","w")

N = int(input())

grid = []
for i in range(N):
    grid.append(list(input().strip()))

visited = [[0]*N for i in range(N)]

group = 0
sizes = {}
for y in range(N):
    for x in range(N):
        if grid[y][x]==".":
            visited[y][x]=1
            continue
        if visited[y][x]==0:
            queue = [(y,x)]
            visited[y][x]=1
        else: continue
        area = 0
        perimeter = 0
        while queue:
            cy,cx = queue.pop()
            visited[cy][cx]=1
            area+=1
            
            surrounding = [(cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)]
            for ccy,ccx in surrounding:
                if not 0<=ccy<N or not 0<=ccx<N: perimeter+=1;continue
                t = grid[ccy][ccx]
                if t == ".":
                    perimeter+=1
                elif t=="#" and visited[ccy][ccx]==0:
                    queue.append((ccy,ccx))
                    visited[ccy][ccx]=-1
        sizes[group] = (area, perimeter)
        group+=1

best = sorted(sizes.values(),key=lambda x:(x[0],-x[1]))[-1]
print(best[0],best[1])