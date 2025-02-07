import sys

sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

N = int(input())
times = []
for i in range(N):
    times.append(list(map(int,input().split())))
times.sort()
currentTime=0
for i in times:
    if i[0]>currentTime:
        currentTime=i[0]+i[1]
    else:
        currentTime+=i[1]
print(currentTime)