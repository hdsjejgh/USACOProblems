import sys
sys.stdin = open("factory.in","r")
sys.stdout = open("factory.out","w")


N = int(input())


mustgo = {}
count = {}

for i in range(N-1):
    a,b = input().split()
    a=int(a)
    b=int(b)
    mustgo[a] = b

for i in range(1,N+1):

    frontier = set([i])
    while len(frontier)!=0:
        node = frontier.pop()
        count[node] = count.get(node,0)+1
        if mustgo.get(node,None) is not None:
            frontier.add(mustgo[node])

for i in count:
    if count[i] == N:
        print(i)
        exit()
print(-1)