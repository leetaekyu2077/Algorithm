import sys
from collections import deque
input = sys.stdin.readline


def rotate(table, n, level):
    offset = 2**level

    for i in range(0, 2**n, offset):
        for j in range(0, 2**n, offset):
            group1, group2, group3, group4 = divide_groups(i, j, table, offset)
            half = offset//2
            # 실질적인 회전 처리 부분
            for k in range(half):

                temp = group4[k] + group1[k]
                for l in range(j, j+offset):
                    table[i+k][l] = temp[l-j]

                temp = group3[k] + group2[k]
                for l in range(j, j+offset):
                    table[i+k+half][l] = temp[l-j]

            # table[i:half] = [group4[i]+group1[i] for i in range(half)]
            # table[i+half:offset] = [group3[i] + group2[i] for i in range(half)]


# 빙하 녹이는 처리 함수
def melt(table, n):
    melted = []
    for i in range(2**n):
        for j in range(2**n):
            # 빙하가 존재할 때만
            if table[i][j] > 0:
                cnt = 0
                # 상하좌우 탐색하면서 인접한 빙하 카운트
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < 2**n and 0 <= nj < 2**n and table[ni][nj] > 0:
                        cnt += 1
                # 3개 이하일 때만 -1 처리
                if cnt < 3:
                    melted.append((i, j))

    for r, c in melted:
        table[r][c] -= 1


def divide_groups(start_r, start_c, table, limit):
    l_half = limit // 2

    group1 = [table[i][start_c:start_c+l_half] for i in range(start_r, start_r+l_half)]
    group2 = [table[i][start_c+l_half:start_c+limit] for i in range(start_r, start_r+l_half)]
    group3 = [table[i][start_c+l_half:start_c+limit] for i in range(start_r + l_half, start_r+limit)]
    group4 = [table[i][start_c:start_c+l_half] for i in range(start_r + l_half, start_r+limit)]

    return group1, group2, group3, group4


def get_total(table):
    total = 0
    for line in table:
        total += sum(line)

    return total


def get_max_group(table, n):
    sizes = [0]
    for i in range(2**n):
        for j in range(2**n):
            if table[i][j] > 0:
                q = deque([(i, j)])
                table[i][j] = 0

                size = 1
                while q:
                    r, c = q.popleft()
                    # 상하좌우 탐색
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nc < 2**n and 0 <= nr < 2**n and table[nr][nc] > 0:
                            size += 1
                            table[nr][nc] = 0
                            q.append((nr, nc))

                sizes.append(size)

    return max(sizes)


def main():
    n, q = map(int, input().split())

    table = []
    for _ in range(2**n):
        table.append(list(map(int, input().split())))
    levels = list(map(int, input().split()))

    for i in range(q):
        rotate(table, n, levels[i])
        melt(table, n)

    print(get_total(table))
    print(get_max_group(table, n))


if __name__ == "__main__":
    main()