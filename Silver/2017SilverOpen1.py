import sys
sys.stdin = open("pairup.in",'r')
sys.stdout = open("pairup.out",'w')

N = int(input())
counts = {}
for i in range(N):
    a,b = map(int,input().split())
    counts[b]=a
cows = sorted(counts.keys())
l,r = 0,N-1
m = 0
while l<=r:
    first = cows[l]
    second = cows[r]

    sub = min(counts[first],counts[second])
    if l==r:
        sub/=2
    counts[first]-=sub
    
    counts[second]-=sub


    if counts[first]==0:
        l+=1
    
    if counts[second]==0:
        r-=1
    
    m = max(m,first+second)

print(m)