import sys
sys.stdin = open("planting.in",'r')
sys.stdout = open("planting.out",'w')

from collections import defaultdict

N = int(input())
connections = defaultdict(list)
for i in range(N-1):
    a,b = map(int,input().split())
    connections[a].append(b)
    connections[b].append(a)
c = [len(connections[i]) for i in range(1,N+1)]
print(max(c)+1)

