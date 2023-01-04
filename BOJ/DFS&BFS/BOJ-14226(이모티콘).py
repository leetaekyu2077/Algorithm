import sys
from collections import deque


N = int(input())
result = sys.maxsize
visited = [[sys.maxsize]*(N+1) for _ in range(N+1)]

q = deque()
q.append((1, 1, 1))     # current_value, clipboard, time

while q:
    current = q.popleft()
    if current[0] > 0 and current[0] <= N and current[1] <= N and current[2] < result:
        if visited[current[0]][current[1]] > current[2]:
            if current[0] != N:
                visited[current[0]][current[1]] = current[2]
                q.append((current[0], current[0], current[2]+1))
                q.append((current[0]+current[1], current[1], current[2]+1))
                q.append((current[0]-1, current[1], current[2]+1))
            else:
                result = current[2]

print(result)