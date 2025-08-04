import sys
sys.stdin = open("leftout.in",'r')
sys.stdout = open("leftout.out",'w')

N = int(input())
cows = []
for i in range(N):
    a = list(map(lambda x:1 if x=='R' else 0,list(input().strip())))
    cows.append(a)

def invert(arr,command):
    item,index = command[0],int(command[1:])-1
    if item=='R':
        arr[index] = [int(not i) for i in arr[index]]
    if item=='C':
        for i in range(N):
            arr[i][index]=int(not arr[i][index])
    return arr

for i in range(N,0,-1):
    if cows[0][i-1]==0:
        cows = invert(cows,f"C{i}")
for i in range(2,N+1):
    if cows[i-1][0]==0:
        cows = invert(cows,f"R{i}")

firstrow = cows[0]
firtcol = [i[0] for i in cows]

ocounts=[i.count(0) for i in cows]
lcounts = [N-i for i in ocounts]



if sum(lcounts)==N**2:
    print(-1)
elif sum(lcounts) == 2*N-1:
    print(1,1)
elif 1 in lcounts:
    print(lcounts.index(1)+1,1)
elif N-1 in lcounts:
    ind = lcounts.index(N-1)
    print(ind+1,cows[ind].index(0)+1)