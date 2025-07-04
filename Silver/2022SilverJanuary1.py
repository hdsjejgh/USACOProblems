N = int(input())
def solve(a,b):
    if a==b:
        return 0
    if a>b:
        return 1+(a%2==1)+solve((a+(a%2==1))//2,b)
    if a<b:
        return min(b-a,1+(b%2==1)+solve(a,b//2))

for i in range(N):
    pair = list(map(int,input().split()))
    c1,c2 = pair
    print(solve(c1,c2))
