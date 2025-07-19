from collections import defaultdict,deque
from math import log10,ceil

def log(n):
    return log10(n)/log10(2)
N = int(input())
connections = defaultdict(list)
for i in range(N-1):
    a,b = map(int,input().split())
    connections[a].append(b)
    connections[b].append(a)
days = 0
queue = deque([1])
explored = set()
def rup(n):
    if int(n)==n:
        return int(n)
    else:
        return ceil(n)
while queue:
    curr = queue.pop()
    explored.add(curr)
    conn = [i for i in connections[curr] if i not in explored]
    if len(conn)==0:
        continue
    days += rup(log(len(conn)+1))+len(conn)
    for i in conn:
        queue.appendleft(i)
print(int(days))
