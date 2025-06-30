X,Y,M = tuple(map(int,open("pails.in", "r").readline().split()))
open("pails.out", "w").write(str(max([M-(((M%X+X*i))%Y) for i in range(0,1+(M//X))]))+'\n')