import sys
from collections import deque
input = sys.stdin.readline

def dfs(x):
    count = 0
    q = deque([x])
    while q:
        curr = q.popleft()
        if not visited[curr]:
            count += 1
            visited[curr] = True
            for com in trust[curr]:
                if not visited[com]:
                    q.append(com)   
    return count

n, m = map(int, input().split())
trust = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    trust[b].append(a)

answers = [0]*(n+1)
for i in range(1, n+1):
    visited = [False]*(n+1)
    answers[i] = dfs(i)

answers = [i for i in range(1, n+1) if answers[i] == max(answers)]
print(*answers, sep=' ')