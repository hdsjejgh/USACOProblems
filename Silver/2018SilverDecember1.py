import sys
sys.stdin  = open("convention.in", "r")
sys.stdout = open("convention.out","w")

N,M,C = map(int,input().split())
cows = list(map(int,input().split()))
cows.sort()
l=0; r=cows[-1]-cows[0]

def possible(time):
    currcars = M
    maxtime,maxcap = cows[0]+time,C-1
    for i in range(N):
        if i<=maxcap and cows[i]<=maxtime:
            continue

        currcars-=1
        if currcars<=0: return False
        maxtime = cows[i]+time
        maxcap=i+C-1

        
    return True

res = -1
while l<=r:
    m = l+(r-l)//2
    p = possible(m)
    if p: 
        res = m
        r = m-1
    elif not p: l = m+1 
print(res)