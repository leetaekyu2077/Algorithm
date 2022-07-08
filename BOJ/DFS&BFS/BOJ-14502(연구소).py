import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
lab = []
empty = []
virus = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    lab.append(temp)
    for j in range(m):
        if temp[j] == 0:
            empty.append((i, j))
        elif temp[j] == 2:
            virus.append((i, j))

# 벽을 세울 수 있는 모든 케이스에 대해 시행
lab_copy = []
all_cases = list(combinations(empty, 3))

max = 0
for case in all_cases:
    lab_copy = [line[:] for line in lab]
    safe_area = 0
    # 세 개의 벽 세우기
    for wall in case:
        lab_copy[wall[0]][wall[1]] = 1
    # 모든 바이러스 퍼뜨리기(BFS)
    for v in virus:
        q = [v]
        visited = []
        while q:
            current = q.pop(0)
            if current not in visited:
                visited.append(current)
                r, c = current[0], current[1]
                lab_copy[r][c] = 2
                if r > 0 and lab_copy[r-1][c] == 0:
                    q.append((r-1, c))
                if c > 0 and lab_copy[r][c-1] == 0:
                    q.append((r, c-1))
                if r < n-1 and lab_copy[r+1][c] == 0:
                    q.append((r+1, c))
                if c < m-1 and lab_copy[r][c+1] == 0:
                    q.append((r, c+1))
    # 안전구역 갯수 세기
    for line in lab_copy:
        safe_area += line.count(0)
    if max < safe_area:
        max = safe_area
print(max)