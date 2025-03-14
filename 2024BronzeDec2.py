N,Q = list(map(int,input().split()))

actions =[]
are = {}
holes = {}
am = 0
for i in range(Q):
    x,y,z = list(map(int,input().split()))
    are[('x',y,z)] = are.get(('x',y,z),0)+1
    
    are[(x,'x',z)] = are.get((x,'x',z),0)+1
    are[(x,y,'x')] = are.get((x,y,'x'),0)+1
    am += 1 if are[('x',y,z)] == N else 0
    am += 1 if are[(x,'x',z)] == N else 0
    am += 1 if are[(x,y,'x')] == N else 0
    print(am)
    
