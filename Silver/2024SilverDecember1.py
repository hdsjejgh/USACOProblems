from itertools import accumulate
T = int(input())

def solve(C):
    b = 0
    e = 0
    p = [0]+list(accumulate(C))

    L = len(C)//2 +1
    minimum = float('inf')
    mid = -1
    for i in range(len(C)-L+1):
        m = p[i+L]-p[i]
        if m<minimum:
            minimum = m
            mid = i-L+2
    b = minimum 

    e = sum(C)-b

    return str(b),str(e)


for i in range(T):
    N = int(input())
    C = list(map(int,input().split()))
    print(' '.join(solve(C)))