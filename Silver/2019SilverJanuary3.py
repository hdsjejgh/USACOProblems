import sys
sys.stdin = open("mountains.in",'r')
sys.stdout = open("mountains.out",'w')

N = int(input())
mountains = []
ranges = []
for i in range(N):
    m = list(map(int,input().split()))
    r = [m[0]-m[1],m[0]+m[1]]
    mountains.append(m)
    ranges.append(r)
ranges.sort()

queue = []
for i in range(len(ranges)):
    if i>=len(ranges): break
    outer = ranges[i]
    c = 0
    expunge = []
    for ii in range(i+1,len(ranges)):
        inner = ranges[ii]
        if inner[0]>=outer[1]: break
        if inner[1]<=outer[1]:
            c+=1
            expunge.insert(0,ii)
    N-=c
    for ii in expunge:
        ranges.pop(ii)
print(N)
