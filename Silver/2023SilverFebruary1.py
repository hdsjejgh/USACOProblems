T = int(input())

for i in range(T):
    input()

    N,tc,tm = map(int,input().split())
    cows = []
    for i in range(N):
        cows.append(list(map(int,input().split())))
    
    def check(money):
        lx, hx = max(1, tc - money), min(tc + tm - money - 1, tc)
        for a,b,c in cows:
            d = tc + tm - money
            if (b - a > 0):
                lx = max(lx, (-c + b * d + (b - a - 1)) // (b - a))
            elif (a - b > 0):
                hx = min(hx, (c - b * d) // (a - b))
            else:
                if (a * d > c):
                    return False
        return lx<=hx


    res = -1
    l = 0; r = tc+tm-2
    while l <= r:
        m = l + (r-l)//2
        status = check(m)
        if status: res = m; r=m-1
        else: l=m+1
    print(res)
    

