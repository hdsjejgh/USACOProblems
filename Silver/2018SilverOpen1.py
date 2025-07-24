import sys
sys.stdin = open("sort.in",'r')
sys.stdout = open("sort.out",'w')

N = int(input())
A = []
for i in range(N):
    A.append((int(input()),i))
A2 = A.copy()
A2.sort(key = lambda x:x[0])
A2 = [A2[i][1] for i in range(N)]
A = [A[i][1] for i in range(N)]
print(1+ max(A2[i]-i for i in range(N)))