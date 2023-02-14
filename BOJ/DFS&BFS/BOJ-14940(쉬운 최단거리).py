import sys
from collections import deque
input = sys.stdin.readline

def getTarget():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                return i, j
            
def checkUnreach():
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0 and distance[i][j] == 0:
                distance[i][j] = -1
    
n, m = map(int, input().split())
board = []
distance = [[0]*m for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input().split())))
target_r, target_c = getTarget()
            
q = deque([(target_r, target_c, 0)])
while q:
    r, c, d = q.popleft()
    if distance[r][c] == 0:
        distance[r][c] = d
        
        if r > 0 and board[r-1][c] != 0:
            q.append((r-1, c, d+1))
        if c < m-1 and board[r][c+1] != 0:
            q.append((r, c+1, d+1))
        if r < n-1 and board[r+1][c] != 0:
            q.append((r+1, c, d+1))
        if c > 0 and board[r][c-1] != 0:
            q.append((r, c-1, d+1))

checkUnreach()
distance[target_r][target_c] = 0

for line in distance:
    print(' '.join(map(str, line)))