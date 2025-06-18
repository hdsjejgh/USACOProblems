import sys
sys.stdin = open("convention2.in","r")
sys.stdout = open("convention2.out","w")


import heapq

N = int(input())
max_wait = 0
current = 0
cows = []
for i in range(N):
    cow = list(map(int,input().split()))
    cow.insert(0,i)
    cows.append(cow)
cows.sort(key=lambda x:x[1],reverse=True)
cowheap = []
while len(cows)!=0 or len(cowheap)!=0:
    if len(cows)!= 0 and cows[-1][1] > current and len(cowheap)==0:
        cow = cows.pop()
        heapq.heappush(cowheap,cow)
        current = cow[1]

    if len(cows)!=0:
        while len(cows)!=0 and cows[-1][1] <= current:
            heapq.heappush(cowheap,cows.pop())
    if len(cowheap)!=0:
        cow = heapq.heappop(cowheap)
        max_wait = max(max_wait,current-cow[1])
        current+=cow[2]
print(max_wait)