import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

max = 1
while q:
    r, c = q.popleft()  
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr, nc = r+dr, c+dc          
        if 0 <= nr < n and 0 <= nc < m and box[nr][nc] == 0:
            q.append((nr, nc))
            box[nr][nc] = box[r][c] + 1  
            max = box[nr][nc]

for line in box:
    for value in line:
        if value == 0:
            print(-1)
            exit(0)
print(max-1)