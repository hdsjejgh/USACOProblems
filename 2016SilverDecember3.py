import sys
sys.stdin = open("moocast.in","r")
sys.stdout = open("moocast.out","w")


from collections import deque

N = int(input())

def dist(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    return (dx*dx+dy*dy)**.5

cows = []
for i in range(N):
    cows.append(list(map(int,input().split())))
max_range = 0
for i,cow in enumerate(cows):
    comm = 0
    explored = set([])
    frontier = deque([i])
    while frontier:
        c = frontier.popleft()
        ccow = cows[c]
        comm+=1
        explored.add(c)
        for ii in range(len(cows)):
            if not ii in frontier and not ii in explored:
                distance = dist(cows[ii][0],cows[ii][1],ccow[0],ccow[1])
                if distance <= ccow[2]:
                    frontier.appendleft(ii)
    max_range = max(comm,max_range)
print(max_range)