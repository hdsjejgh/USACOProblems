import sys
sys.stdin  = open("hps.in",'r')
sys.stdout = open("hps.out",'w')

conv = {"H":0,"P":1,"S":2}
N,K = map(int,input().split())
moves = []
for i in range(N):
    moves.append(conv[input().strip()])

dp = [[[0,0,0] for i in range(K+1)] for i in range(N+1)]

for n in range(N):
    for k in range(K+1):
        for m in range(3):
            if m == moves[n]:
                dp[n][k][m] += 1

            if k!=K:
                dp[n+1][k+1][0] = max(dp[n+1][k+1][0],dp[n][k][m])
                dp[n+1][k+1][1] = max(dp[n+1][k+1][1],dp[n][k][m])
                dp[n+1][k+1][2] = max(dp[n+1][k+1][2],dp[n][k][m])
            dp[n+1][k][m]=max(dp[n+1][k][m],dp[n][k][m])

ans = 0
for m in range(3):
	ans = max(ans, dp[N - 1][K][m])
print(ans)