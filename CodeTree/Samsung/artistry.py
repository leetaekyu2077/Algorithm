import sys
from collections import deque
input = sys.stdin.readline


def get_groups(n, drawing):
    groups = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                num = drawing[i][j]
                group = []

                q = deque([(i, j)])
                while q:
                    ci, cj = q.popleft()
                    if visited[ci][cj]:
                        continue

                    visited[ci][cj] = True
                    group.append((ci, cj))
                    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < n and 0 <= nj < n and drawing[ni][nj] == num:
                            q.append((ni, nj))

                groups.append(sorted(group))

    return groups


def get_score(n, drawing, groups):
    score = 0
    length = len(groups)

    for i in range(length):
        group1 = groups[i]
        for j in range(i+1, length):
            group2 = groups[j]
            border_length = get_border(n, group1, groups[j])

            score += ((len(group1) + len(group2))
                      * drawing[group1[0][0]][group1[0][1]]
                      * drawing[group2[0][0]][group2[0][1]]
                      * border_length)

    return score


def get_border(n, group1, group2):
    # 확인하고 싶은 두 그룹만 표시된 테이블
    table = [[0]*n for _ in range(n)]
    border_length = 0

    # 두 그룹을 각각 1, 2로 표시
    for i, j in group1:
        table[i][j] = 1
    for i, j in group2:
        table[i][j] = 2

    for ci, cj in group1:
        for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < n and 0 <= nj < n and table[ni][nj] == 2:
                border_length += 1

    return border_length


def rotate_cross(n, drawing):
    row = drawing[n//2][::-1]
    col = list(list(zip(*drawing))[n//2])

    drawing[n//2] = col
    for i in range(n):
        drawing[i][n//2] = row[i]


def rotate_square(start, end, drawing):
    sr, sc = start[0], start[1]
    er, ec = end[0], end[1]

    temp = []
    for line in drawing[sr:er]:
        temp.append(line[sc:ec])

    temp = [list(line) for line in list(zip(*temp[::-1]))]

    for i in range(sr, er):
        for j in range(sc, ec):
            drawing[i][j] = temp[i-sr][j-sc]


def main():
    n = int(input())
    drawing = []
    for _ in range(n):
        drawing.append(list(map(int, input().split())))

    answer = 0
    for i in range(4):
        # 점수 계산
        groups = get_groups(n, drawing)
        answer += get_score(n, drawing, groups)

        if i == 3:
            break

        # 회전
        rotate_cross(n, drawing)    # 십자가 회전
        rotate_square((0, 0), (n//2, n//2), drawing)    # 왼쪽 상단
        rotate_square((0, n//2+1), (n//2, n), drawing)  # 오른쪽 상단
        rotate_square((n//2+1, 0), (n, n//2), drawing)     # 왼쪽 하단
        rotate_square((n//2+1, n//2+1), (n, n), drawing)   # 오른쪽 하단

    print(answer)


if __name__ == "__main__":
    main()
