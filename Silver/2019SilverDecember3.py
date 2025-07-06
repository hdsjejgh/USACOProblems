import sys
sys.stdin = open("milkvisits.in","r")
sys.stdout = open("milkvisits.out","w")

from collections import defaultdict

N,M = map(int,input().split())
breeds = list(input())
connections = defaultdict(list)
for i in range(N-1):
    c1,c2 = map(int,input().split())
    connections[c1].append(c2)
    connections[c2].append(c1)
ans = []

components = {}
count = 0
Gexc,Hexc=defaultdict(list),defaultdict(list)

explored = set([])
for i in range(1,N+1):
    if i in explored:
        continue
    group = count
    count+=1
    b = breeds[i-1]
    frontier = [i]
    while frontier:
        node = frontier.pop()
        explored.add(node)
        con = connections[node]
        components[node]=group
        for c in con:
            if c not in explored and breeds[c-1]==b:
                frontier.append(c)



for i in range(M):
    s,e,b = input().split()
    s=int(s); e=int(e)
    if breeds[s-1]==b or breeds[e-1]==b:
        ans.append('1')
    else:
        if components[s]==components[e]:
            ans.append('0')
        else:
            ans.append('1')
print(''.join(ans))