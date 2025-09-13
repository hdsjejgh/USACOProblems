N = int(input())
cows = list(map(int, input().split()))

ans = 0
stack = []

for i, h in enumerate(cows):
    while stack and stack[-1][0] < h:
        stack.pop()
    if stack:
        ans += i - stack[-1][1] + 1
    stack.append((h, i))

stack = []

for i in range(N-1, -1, -1):
    h = cows[i]
    while stack and stack[-1][0] < h:
        stack.pop()
    if stack:
        ans += stack[-1][1] - i + 1
    stack.append((h, i))

print(ans)