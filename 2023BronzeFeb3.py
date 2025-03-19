N, K = list(map(int,input().split()))
N+=K
schedule = list(map(int,input().split()))
for i in range(len(schedule)-1):
    N+=min(schedule[i+1]-schedule[i]-1,K)
print(N)