import sys
sys.stdin = open("lemonade.in","r")
sys.stdout = open("lemonade.out","w")
N = int(input())
cows = sorted(list(map(int,input().split())),reverse=True)
c = 0
for i in cows:
    if i>=c:
        c+=1
print(c)