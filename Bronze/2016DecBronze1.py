import sys
sys.stdin = open("diamond.in", "r")
sys.stdout = open("diamond.out", "w")

N,K = map(int,input().split())
diamonds = []
for i in range(N):
    diamonds.append(int(input()))
diamonds.sort()
maxNum =0
sub = (diamonds[i:ii] for i in range(len(diamonds)) for ii in range(i + 1, len(diamonds) + 1))
for s in sub:
    if s[-1]-s[0]<=K:
        maxNum=max(maxNum,len(s))
print(maxNum)