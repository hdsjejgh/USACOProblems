n,k = map(int,input().split())

def ask(q,a,b):

    print(f"{q} {a} {b}",flush=True)
    return int(input())
    return eval(f"{nu[a-1]}{d[q]}{nu[b-1]}")

def sum(a,b):
    a+=1
    b+=1
    and_ = ask('and',a,b)
    or_ = ask('or',a,b)
    return 2*and_ + (~and_ & or_)

nums = []
ab = sum(0,1)
bc = sum(1,2)
ac = sum(0,2)
a = (ab+ac-bc)//2
b = ab-a
c = ac-a
nums+=[a,b,c]

for i in range(3,n):
    ai = sum(0,i)
    i=ai-a
    nums.append(i)

nums.sort()
print(f"finish {nums[k-1]}")