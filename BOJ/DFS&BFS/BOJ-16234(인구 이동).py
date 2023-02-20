import sys
from collections import deque
input = sys.stdin.readline

def makeUnion(row, col, day):
    q = deque([(row, col)])
    union = [(row, col)]
    visited[row][col] = day
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                if visited[ni][nj] < day and (l <= abs(lands[i][j] - lands[ni][nj]) <= r):
                    visited[ni][nj] = day
                    q.append((ni, nj))
                    union.append((ni, nj))  
    
    return union if len(union) > 1 else None
                    
def avgUnion(union):
    global lands, q
    p = 0
    for x, y in union:
        p += lands[x][y]
    avg = p // len(union)
    
    for x, y in union:
        lands[x][y] = avg
        q.append((x, y))

n, l, r = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(n)]
visited = [[-2]*n for _ in range(n)]
day = -1
q = deque([(i, j) for i in range(n) for j in range(n)])

while q:
    unions = []
    while q:
        i, j = q.popleft()
        if visited[i][j] < day:
            temp = makeUnion(i, j, day)
            if temp:
                unions.append(temp)   
                
    for union in unions:
        avgUnion(union)
    day += 1

print(day)