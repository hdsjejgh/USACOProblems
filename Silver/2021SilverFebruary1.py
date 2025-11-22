N = int(input())
grid = [[False] * 2000 for i in range(2000)] 
q = []
dx,dy = [1,0,-1,0], [0,1,0,-1]

def count(x,y,v):
    c=0
    for i in range(4):
        if v[y+dy[i]][x+dx[i]]: c+=1
    return c

def empty(x,y,v):
    for i in range(4):
        if not v[y+dy[i]][x+dx[i]]: return (x+dx[i],y+dy[i])

def check(x,y,v,q):
    if count(x,y,v) !=3: return
    emp = empty(x,y,v)
    q.append(emp)

total=0
for _ in range(1,N+1):
    
    x1,y1 = map(int,input().split())
    x1+=500; y1+=500
    q.append((x1,y1))

    c=0
    while q:
        x,y = q.pop()
        if grid[y][x]: continue
        total+=1
        grid[y][x]=True
        check(x,y,grid,q)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if grid[ny][nx]:
                check(nx,ny,grid,q)
        
    print(total-_)