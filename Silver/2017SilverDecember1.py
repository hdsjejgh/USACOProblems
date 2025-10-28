import sys
sys.stdin = open("homework.in","r")
sys.stdout = open("homework.out","w")

N = int(input())
W = list(map(int,input().split()))

m = 0
s = sum(W)
p = []
for i in range(N-2):
    s-=W[i]
    avg = s * (1/(N-1-i))
    if avg > m:
        p = [str(i+1)]
        m=avg
    elif avg == m:
        p.append(str(i+1))

print("\n".join(p))