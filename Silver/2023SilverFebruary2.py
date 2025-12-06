from bisect import bisect_right

G,N = map(int,input().split())
grazings = []
for i in range(G):
    g = list(map(int,input().split()))
    g = [g[2],g[0],g[1]]
    grazings.append(g)
grazings.sort()
alibis = []
for i in range(N):
    g = list(map(int,input().split()))
    g = [g[2],g[0],g[1]]
    alibis.append(g)
alibis.sort()

def dist(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)

c= N
for i in range(N):
    cow = alibis[i]
    t,x,y=cow
    point = bisect_right(grazings,cow)
    if point == 0:
        p1=True
    else:
        tg,xg,yg = grazings[point-1]
        d = dist(x,y,xg,yg)
        dt = abs(t-tg)**2
        p1 = (d<=dt)
    if point == G:
        p2=True
    else:
        tg,xg,yg = grazings[point]
        d = dist(x,y,xg,yg)
        dt = abs(tg-t)**2
        p2 = (d<=dt)
    if p1 and p2: c-=1
print(c)