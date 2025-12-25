import sys
sys.stdin = open("cardgame.in","r")
sys.stdout = open("cardgame.out","w")
import bisect

N = int(input())
opp = []
oppset = set([])
for i in range(N):
    n = int(input())
    opp.append(n)
    oppset.add(n)
cards = [i for i in range(1,N*2+1) if i not in oppset]
hcard = opp[:N//2]
lcard = opp[N//2:]
bh = cards[N//2:]
bl = cards[:N//2]

hcard.sort(reverse=True)
lcard.sort(reverse=False)
bh.sort(reverse=True)
bl.sort(reverse=False)

points = 0
bindex = 0
for i in range(N//2):
    if bh[bindex]>hcard[i]:
        bindex+=1
        points+=1

bindex = 0
for i in range(N//2):
    if bl[bindex]<lcard[i]:
        bindex+=1
        points+=1

print(points)