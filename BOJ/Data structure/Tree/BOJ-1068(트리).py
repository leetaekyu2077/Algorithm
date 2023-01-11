import sys
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
target = int(input())

stk = [target]
while stk:
    curr = stk.pop()
    parents[curr] = -2   
    for i in range(n):
        if parents[i] == curr:
            stk.append(i)

answer = 0
for i in range(n):
    if parents[i] != -2 and i not in parents:
        answer += 1
print(answer)