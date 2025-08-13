import sys
sys.stdin  = open("multimoo.in",'r')
sys.stdout = open("multimoo.out",'w')
from collections import deque,defaultdict

N = int(input())
board = []
for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)
explored = [[False]*N for i in range(N)]
groups = {}
g = 0
c2g = {}
types = set()
for y in range(N):
    for x in range(N):
        if not explored[y][x]:
            cow = board[y][x]
            types.add(cow)
            queue = deque([(x,y)])
            current = []
            while queue:
                xi,yi = queue.pop()
                c2g[(xi,yi)]=g
                current.append((xi,yi))
                explored[yi][xi]=True
                potential = [(xi-1,yi),(xi+1,yi),(xi,yi-1),(xi,yi+1)]
                for adj in potential:
                    xi,yi = adj
                    if 0<=xi<N and 0<=yi<N and board[yi][xi]==cow and not explored[yi][xi] and (xi,yi) not in queue:
                        queue.appendleft((xi,yi))
            groups[g]=(len(current),current,cow)
            g+=1
group_connections = {}
for i in range(g):
    conn = set()
    _,cows,_ = groups[i]
    for c in cows:
        xi,yi = c
        potential = [(xi-1,yi),(xi+1,yi),(xi,yi-1),(xi,yi+1)]
        for p in potential:
            xi,yi = p
            if 0<=xi<N and 0<=yi<N and c2g[(xi,yi)]!=i:
                conn.add((board[yi][xi],c2g[(xi,yi)]))
    group_connections[i]=conn

c2c = {}
for g1 in range(g):
    _,cows,_ = groups[g1]
    c1 = board[cows[0][1]][cows[0][0]]
    curr_conn = defaultdict(list)
    for color, g2 in group_connections[g1]:
        curr_conn[color].append(g2)
    for color in curr_conn:
        valid_g = [g1]
        queue = deque(curr_conn[color])
        while queue:
            group = queue.pop()
            valid_g.append(group)
            for gg in group_connections[group]:
                col,gro = gg
                if gro not in queue and gro not in valid_g and (col == c1 or col == color):
                    queue.appendleft(gro)
        c2c[(min(c1,color),max(c1,color))] = sum(groups[i][0] for i in valid_g)


print(max(groups.values())[0])
print(max(c2c.values()))