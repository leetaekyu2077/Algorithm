import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, j, cnt):
    global m, group
    m[i][j] = 0
    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and m[ni][nj] == 1:
            cnt = dfs(ni, nj, cnt+1) 
    return cnt            

n = int(input())
m = [list(map(int, input().rstrip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(n):
        if m[i][j] == 1:
            answer.append(dfs(i, j, 1))

answer.sort()
print(len(answer))
print(*answer, sep='\n')