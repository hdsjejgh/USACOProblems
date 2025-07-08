import sys
sys.stdin = open("closing.in",'r')
sys.stdout = open("closing.out",'w')

from bisect import bisect_left
from collections import defaultdict
N,M = map(int,input().split())
connections = defaultdict(list)
o = [i for i in range(1,N+1)]
for i in range(M):
    b1,b2 = map(int,input().split())
    connections[b1].append(b2)
    connections[b2].append(b1)

def solve():
    b = o[0]
    frontier = [b]
    explored = set([])
    while frontier:
        current = frontier.pop()
        explored.add(current)
        possible = connections[current]
        for i in possible:
            if i not in explored and i not in frontier:
                frontier.append(i)
    if len(explored)==len(o):
        return "YES"
    return "NO"

for i in range(N):
    if len(o)==0:
        print('YES')
        break
    print(solve())
    b = int(input())
    o.pop(bisect_left(o,b))
    connected = connections.pop(b)
    for c in connected:
        connections[c].pop(connections[c].index(b))
    