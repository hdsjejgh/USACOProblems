import sys
sys.stdin = open("hps.in","r")
sys.stdout = open("hps.out","w")

N = int(input())
moves = [input().strip() for i in range(N)]
hwins = []
pwins = []
swins = []
h,p,s = 0,0,0
for i in range(N):
    m = moves[i]
    if m == "H": p+=1
    elif m == "S": h+=1
    elif m == "P": s+=1

    hwins.append(h)
    swins.append(s)
    pwins.append(p)
# hwins.append(0)
# swins.append(0)
# pwins.append(0)

maximum = 0
for i in range(N):
    before = max(hwins[i],swins[i],pwins[i])
    after = max(hwins[N-1]-hwins[i],swins[N-1]-swins[i],pwins[N-1]-pwins[i])
    maximum=max(before+after,maximum)
print(maximum)
