import sys
sys.stdin  = open("reststops.in",'r')
sys.stdout = open("reststops.out",'w')

l,n,rf,rb = map(int,input().split())
stops = []
for i in range(n):
    stops.append(list(map(int,input().split())))
stops.sort(key=lambda x:x[0],reverse=True)
viable = []
m=0
for i in stops:
    if i[1]>m:
        viable.append(i)
        m = i[1]
viable = viable[::-1]
total = 0
posf,posb = 0,0
prev = 0
for i in viable:
    point = i[0]
    dist = point-prev
    ftime = dist * rf
    btime = dist * rb
    rtime = ftime-btime
    prev = point
    total+=rtime*i[1]
print(total)