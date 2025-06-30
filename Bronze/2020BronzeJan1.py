import sys
sys.stdin = open("word.in","r")
sys.stdout = open("word.out","w")

N,K=input().split()
K = int(K)
text = input().split()
line = []
for word in text:
    if sum(map(len,line))+len(word)<=K:
        line.append(word)
        continue
    print(' '.join(line))
    line=[word]
if len(line)!=0:
    print(' '.join(line))
