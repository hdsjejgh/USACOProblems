import sys
sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out","w")

N = int(input())
pos = []
for i in range(N):
    pos.append(int(input()))
pos.sort()
maxBales = 0

def find(bale: int):
    global maxBales
    posc = pos.copy()
    bales = {bale: 1}
    count = 0
    explored = set([bale])

    while bales:
        b = tuple(bales.keys())[-1]
        radius = bales[b]
        explored.add(b)
        del bales[b]
        count+=1
        for i in range(b+1,b+1+radius):
            if i in posc and i not in explored and i not in bales.keys():
                bales[i] = radius+1
        for i in range(b-1,b-1-radius,-1):
            if i in posc and i not in explored and i not in bales.keys():
                bales[i] = radius+1
    maxBales = max(maxBales,count)




    
for idx, bale in enumerate(pos):
    find(bale)
print(maxBales)