import sys
sys.stdin = open("split.in","r")
sys.stdout = open("split.out","w")

N = int(input())
cows = []
minx,miny,maxx,maxy=[-1]*4
for i in range(N):
    x,y = map(int,input().split())
    cows.append([x,y])

ans=0
def upd(x,y):
    return (min(x[0],y),max(x[1],y))

def search():
    global ans
    cows.sort()

    pref = [(cows[0][1], cows[0][1])]
    for i in range(1,N): pref.append(upd(pref[-1],cows[i][1]))

    suff =  [(cows[-1][1], cows[-1][1])]
    for i in range(N-2,-1,-1): suff.append(upd(suff[-1],cows[i][1]))
    suff.reverse()

    area = (cows[-1][0] - cows[0][0]) * (pref[-1][1] - pref[-1][0])
    best = float("inf")

    for i in range(N-1):
        if cows[i][0]!=cows[i+1][0]:
            r1 = (cows[i][0] - cows[0][0]) * (pref[i][1] - pref[i][0])
            r2 = (cows[-1][0] - cows[i+1][0]) * (suff[i+1][1] - suff[i+1][0])
            best = min(best,r1+r2)
    return area-best

ans = max(ans,search())
cows = [[y,x] for x,y in cows]
ans = max(ans,search())
print(ans)