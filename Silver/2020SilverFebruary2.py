import sys
sys.stdin = open("triangles.in",'r')
sys.stdout = open("triangles.out",'w')

from collections import defaultdict
from itertools   import accumulate
from bisect      import bisect_left

M = 10**9 + 7
N = int(input())
fences = []
Xs,Ys = defaultdict(list),defaultdict(list)
for i in range(N):
    x,y = map(int,input().split())
    f = [x,y]
    Xs[x].append(y)
    Ys[y].append(x)
    fences.append(f)
for x in Xs:
    Xs[x].sort()
for y in Ys:
    Ys[y].sort()
x_pre = Xs.copy()
y_pre = Ys.copy()
for x in x_pre:
    x_pre[x] = [0]+list(accumulate(x_pre[x]))
for y in y_pre:
    y_pre[y] = [0]+list(accumulate(y_pre[y]))


s = 0
for f in fences:
    x,y = f
    x_index = bisect_left(Xs[x], y)
    y_index = bisect_left(Ys[y], x)
    x_sum = (
		y * x_index
		- x_pre[x][x_index]
		+ x_pre[x][len(Xs[x])]
		- x_pre[x][x_index + 1]
		- (y * (len(Xs[x]) - x_index - 1))
	)

    y_sum = (
    	x * y_index
    	- y_pre[y][y_index]
    	+ y_pre[y][len(Ys[y])]
    	- y_pre[y][y_index + 1]
    	- (x * (len(Ys[y]) - y_index - 1))
    )

    s+=y_sum*x_sum
print(int(s%M))
