from collections import deque
import sys
sys.stdin = open("circlecross.in","r")
sys.stdout = open("circlecross.out","w")

s = list(input())
active = []
a2 = set([])
pairs = set([])
for i in s:
    if i in a2:
        for ii in active:
            if ii == i:
                a2.remove(i)
                active.pop(active.index(i))
                break
            h = [i,ii]
            h.sort()
            pairs.add(tuple(h))
    else:
        a2.add(i)
        active = [i]+active

print(len(pairs))