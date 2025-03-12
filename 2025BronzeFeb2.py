N = int(input())
arr = list(map(int,input().split()))
count = [0] * (N+1)
for i in arr:
    count[i]+=1
c = 0
for i in range(len(count)):
    print(max(count[i],c))
    if count[i]==0:
        c+=1
