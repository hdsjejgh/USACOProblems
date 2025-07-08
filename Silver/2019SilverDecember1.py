import sys
sys.stdin = open("moobuzz.in",'r')
sys.stdout = open("moobuzz.out",'w')

N = int(input())
m=(N-1)//8
nn=15*m
print(nn+[14,1,2,4,7,8,11,13][N%8])