N, K = map(int,input().split())
positions = [i for i in range(1,N+1)]
counter = {i:set([i]) for i in range(1,N+1)}
for i in range(K):
    a,b = map(int,input().split())
    counter[positions[a-1]].add(b)
    counter[positions[b-1]].add(a)
    positions[a-1],positions[b-1] = positions[b-1],positions[a-1]
unique = []
for i in range(1,N+1):
    amount = counter[i]
    ii = positions[i-1]
    while ii!=i:
        if ii<i:
            amount|=unique[ii-1]
            break
        amount |= counter[ii]
        ii = positions[ii-1]
    unique.append(amount)
    print(len(amount))