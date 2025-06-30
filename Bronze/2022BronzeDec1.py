input()
cows = list(map(int,input().split()))
cows.sort(reverse=True)
m = 0
maxcost = 0
for i in range(len(cows)):
    amount = cows[i] *(i+1)
    if amount >= m:
        m = amount
        maxcost=cows[i]
print(m, maxcost)