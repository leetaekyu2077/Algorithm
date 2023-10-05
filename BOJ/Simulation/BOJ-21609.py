import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, table):
    answer = 0

    while True:
        groups = get_groups(n, table)

        if not groups:
            return answer
        
        # 가장 큰 그룹을 찾는 정렬 조건에 맞춰 정렬
        groups.sort(key=lambda x: (len(x), x[-1], x[0][0], x[0][1]), reverse=True)
        biggest = groups[0]

        # 가장 큰 그룹 제거 후 점수 계산
        answer += remove_biggest(biggest, table)
        # 중력, 회전, 중력 적용
        apply_gravity(n, table)
        table = rotate(table)
        apply_gravity(n, table)

# 전체 테이블에서 모든 그룹을 탐색하고, 그 정보를 저장한 배열을 반환
def get_groups(n, table):
    groups = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and table[i][j] > 0:
                # 그룹 탐색 전 초기화
                visited[i][j] = True
                captain = (i, j)
                rainbows = []
                
                # 그룹 탐색 시작
                q = deque([captain])
                group = [captain]

                while q:
                    r, c = q.popleft()
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n:
                            if (not visited[nr][nc] and 
                                (table[nr][nc] == 0 or table[nr][nc] == table[captain[0]][captain[1]])):
                                visited[nr][nc] = True
                                q.append((nr, nc))
                                group.append((nr, nc))
                                if table[nr][nc] == 0: rainbows.append((nr, nc))

                if len(group) > 1:
                    group.append(len(rainbows))
                    groups.append(group)

                for r, c in rainbows:
                    visited[r][c] = False

    return groups

def remove_biggest(biggest, table):
    for r, c in biggest[:-1]:
        # 가장 큰 그룹의 블럭 위치에 대하여 제거 처리
        table[r][c] = -2

    return len(biggest[:-1])**2

def apply_gravity(n, table):
    for c in range(n):
        for r in range(n-1, -1, -1):
            if table[r][c] != -1 and table[r][c] != -2:
                row = r
                while row < n-1 and table[row+1][c] == -2:
                    row += 1
                if r != row:
                    table[row][c] = table[r][c]
                    table[r][c] = -2

def rotate(table):
    temp = []
    for line in zip(*table):
        temp.append(list(line))

    return temp[::-1]


def main():
    n, m = map(int, input().split())
    table = []
    for _ in range(n):
        table.append(list(map(int, input().split())))

    print(solution(n, m, table))

if __name__ == "__main__":
    main()