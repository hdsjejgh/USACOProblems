import sys
sys.stdin  = open("mooyomooyo.in",'r')
sys.stdout = open("mooyomooyo.out",'w')

N,K = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,list(input().strip()))))

def printb(b):
    for i in b:
        print(''.join(map(str,i)))

def get_regions(b):
    _=0
    regions = {}
    explored = [[False for i in range(10)] for ii in range(N)]
    for y in range(N):
        for x in range(10):
            if b[y][x]!=0 and not explored[y][x]:
                queue = [(y,x)]
                color = b[y][x]
                
                group = []
                while queue:
                    cy,cx = queue.pop()
                    if b[cy][cx]==color:
                        explored[cy][cx]=True
                        group.append((cy,cx))
                        possible = [(cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)]
                        for yy,xx in possible:
                            if 0<=xx<10 and 0<=yy<N and not explored[yy][xx] and (yy,xx) not in queue:
                                queue.append((yy,xx))
                if len(group)>=K:
                    regions[_]=group
                    _+=1
    return regions

def transpose(b):
    return [list(row) for row in zip(*b)]

def clear(b,regions):
    for i in regions:
        squares = regions[i]
        for sqy,sqx in squares:
            b[sqy][sqx]=0
    b = transpose(b)
    for i,row in enumerate(b):
        row = [i for i in row if i!=0]
        row = ([0]*(N-len(row)))+row
        b[i]=row
    return transpose(b)

while True:
    r=get_regions(board)
    if len(r)==0: break
    board = clear(board,r)

printb(board)