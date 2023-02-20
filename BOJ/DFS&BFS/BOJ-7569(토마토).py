import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for z in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[z][y][x] == 1:
                q.append((z, y, x))

step = [(0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
max = 1
while q:
    z, y, x = q.popleft()
    for dz, dy, dx in step:
        nz, ny, nx = z+dz, y+dy, x+dx
        if (0 <= nz < h and 0 <= ny < n and 0 <= nx < m and
            boxes[nz][ny][nx] == 0):            
            q.append((nz, ny, nx))
            max = boxes[z][y][x] + 1
            boxes[nz][ny][nx] = max

for box in boxes:
    for line in box:
        if 0 in line:
            print(-1)
            exit(0)
print(max-1)