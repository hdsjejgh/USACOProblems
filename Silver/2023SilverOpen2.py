from collections import defaultdict

C,N = map(int,input().split())
teams = [0]*N
min_edits = [float("inf")] * (1 << C)

for i in range(N):
    team = input()
    for ii in range(C):
        if team[ii] == "G":
            teams[i] += 1 << (C - ii - 1)

    min_edits[teams[i]] = 0

for mask in range(1 << C):
    for edit in range(C):
        if min_edits[mask] != float("inf"):
            min_edits[mask ^ (1 << edit)] = min(
                min_edits[mask ^ (1 << edit)], min_edits[mask] + 1
            )

for i in range(N):
    print(C - min_edits[teams[i] ^ ((1 << C) - 1)])