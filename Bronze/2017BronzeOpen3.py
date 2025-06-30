import sys
sys.stdin = open("art.in","r")
sys.stdout = open("art.out","w")

N=int(input())
canvas=[]

for i in range(N):
    canvas.append(list(map(int,list(input()))))



flatCanvas = set(canvas[i][ii] for i in range(N) for ii in range(N))
possible = set(filter(lambda x:x!=0,set(flatCanvas)))



def getRange(positions):
    L,R,T,B = positions
    return [canvas[i][ii] for i in range(T,B+1) for ii in range(L,R+1)]

def findRange(color):
    if not color in flatCanvas:
        return None
    L,R,T,B = -1,-1,-1,-1
    for i in range(N):
        if L == -1 and color in set(canvas[ii][i] for ii in range(len(canvas))):
            L=i
        if T == -1 and color in canvas[i]:
            T=i
    for i in range(N-1,-1,-1):
        if R == -1 and color in set(canvas[ii][i] for ii in range(len(canvas))):
            R=i
        if B == -1 and color in canvas[i]:
            B=i
    return (L,R,T,B)

removes=set()
for i in possible:
    r = getRange(findRange(i))
    for ii in r:
        if ii!=i:
            removes.add(ii)
print(len(possible)-len(removes))

