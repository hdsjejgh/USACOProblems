from bisect import bisect_right
N,Q = map(int,input().split())
fence = list(input().strip())

prefix =[0,]
stack = []
strokes = []
count = 0
for color in fence:
    if len(strokes)==0:
        strokes.append(color)
        count+=1
        
    elif color==strokes[-1]: #if same color
        pass
    elif color > strokes[-1]: #if color darker
        strokes.append(color)
        count+=1
    elif color < strokes[-1]: #color lighter
        point = bisect_right(strokes,color)
        p1,p2 = strokes[:point],strokes[point:]
        strokes=p1
        if len(p1)==0 or p1[-1]!=color:
            strokes.append(color)
            count+=1
    prefix.append(count)

fence = fence[::-1]
suffix =[0,]
stack = []
strokes = []
count = 0
for color in fence:
    if len(strokes)==0:
        strokes.append(color)
        count+=1
        
    elif color==strokes[-1]: #if same color
        pass
    elif color > strokes[-1]: #if color darker
        strokes.append(color)
        count+=1
    elif color < strokes[-1]: #color lighter
        point = bisect_right(strokes,color)
        p1,p2 = strokes[:point],strokes[point:]
        strokes=p1
        if len(p1)==0 or p1[-1]!=color:
            strokes.append(color)
            count+=1
    suffix.append(count)

for i in range(Q):
    a,b = map(int,input().split())
    part1 = prefix[a-1]
    part2 = suffix[N-b]
    print(part1+part2)