import sys
sys.stdin = open("lifeguards.in", "r")
sys.stdout = open("lifeguards.out", "w")
qjiwofjqf = int(input()) 
ranges = [] 
totals=[]
for i in range(qjiwofjqf):
    a,b = map(int,input().split())
    ranges.append(set (range(a+1,b+1)))
for i,v in enumerate (ranges):
    newranges = ranges.copy()
    newranges.pop(i)
    newset = set()
    for j in newranges:
        newset = newset.union(j)
    totals.append(len(newset))
print(max(totals))