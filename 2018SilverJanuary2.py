import sys
sys.stdin = open("rental.in","r")
sys.stdout = open("rental.out","w")

from bisect import bisect_left,bisect_right
from itertools import accumulate
N,M,R = list(map(int,input().split()))
cows = []
for i in range(N):
    cows.append(int(input()))
orders = []
for i in range(M):
    orders.append(list(map(int,input().split())))
rents = []
for i in range(R):
    rents.append(int(input()))

cows.sort(reverse=True)
rents.sort(reverse=True)
orders.sort(key=lambda x:x[1],reverse=True)

or1=[i[0] for i in orders]
or2=[i[1] for i in orders]
or1=list(accumulate(or1))
or2=list(accumulate(or2))
orderp = [orders[i][1]*orders[i][0] for i in range(M)]
orderp = list(accumulate(orderp))


money = 0

cowp = list(accumulate(cows))
rentp = list(accumulate(rents))

for i in range(N+1):
    milk = cowp[i-1] if i!=0 else 0
    profit = 0
    left = N-i
    renting = min(R,left)
    profit+= rentp[renting-1] if renting !=0 else 0
    ind = bisect_left(or1,milk)
    left_milk = milk - (or1[ind-1] if ind else 0)
    if ind < M:
        profit += left_milk * orders[ind][1]
    profit+=orderp[ind-1] if ind!= 0 else 0
    money = max(profit,money)

print(money)


