import sys
sys.stdin = open("shuffle.in","r")
sys.stdout = open("shuffle.out","w")

N = int(input())
cows = list(map(lambda x:int(x)-1,input().split()))
count = 0
explored = set()
counted = set()
outer = False
for i,move in enumerate(cows):
    if i not in explored:
        explored.add(i)
        t = move
        h = cows[move]
        while t!=h:
            if t in counted or h in counted:
              outer = True
              break
            explored.add(t)
            explored.add(h)
            t=cows[t]
            h=cows[cows[h]]
        if outer:
            outer=False
            continue
        counted.add(t)
        count+=1
        t=cows[t]
        while t!=h:
            counted.add(t)
            count+=1
            explored.add(t)
            t=cows[t]


print(count)
            