import sys
sys.stdin = open("gates.in",'r')
sys.stdout = open("gates.out",'w')
N = int(input())
moves = list(input().strip())
pos = [0,0]
reached = set([(0,0)])
reachedpairs = set()
count = 0
for move in moves:
    prev = (pos[0],pos[1])
    if move=='N':
        pos = (pos[0],pos[1]+1)
    if move=='S':
        pos = (pos[0],pos[1]-1)
    if move=='E':
        pos = (pos[0]+1,pos[1])
    if move=='W':
        pos = (pos[0]-1,pos[1])


    if pos in reached:
        if (prev,pos) not in reachedpairs and (pos,prev) not in reachedpairs:
            count+=1
    reached.add(pos)
    reachedpairs.add((prev,pos))
print(count)