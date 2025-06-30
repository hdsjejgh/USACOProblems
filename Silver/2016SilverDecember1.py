import sys


sys.stdin = open("haybales.in", "r")

sys.stdout = open("haybales.out", "w")


import bisect
N,Q = list(map(int,input().split()))
bales = list(map(int,input().split()))
bales=sorted(bales)
for i in range(Q):
    l,r = list(map(int,input().split()))
    id1 = bisect.bisect_left(bales,l)
    id2 = bisect.bisect_right(bales,r)
    print(id2-id1)