import sys
sys.stdin = open("mootube.in","r")
sys.stdout = open("mootube.out","w")


from collections import defaultdict, deque


N, Q = map(int,input().split())
tree = defaultdict(list)

for i in range(N-1):
    edge = list(map(int,input().split()))
    tree[edge[0]].append((edge[1],edge[2]))
    tree[edge[1]].append((edge[0],edge[2]))
for i in range(Q):
    k,v = map(int,input().split())
    frontier = deque([v])
    explored = set()
    count = -1
    while frontier:
        node = frontier.pop()
        explored.add(node)
        count+=1
        connections = tree[node]
        for n,r in connections:
            if r < k:
                continue
            if n not in explored:
                frontier.append(n)
    print(count)