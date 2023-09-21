import sys
input = sys.stdin.readline

results = []
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def move_fishes(table, shark):

    new_table = [[info[:] for info in line] for line in table]
    indices = {}

    for i in range(4):
        for j in range(4):
            if new_table[i][j][0] > 0:
                indices[new_table[i][j][0]] = (i, j)

    for i in range(1, 17):    
        if i not in indices or indices[i] == shark:
            continue

        r, c = indices[i]
        direct = new_table[r][c][1]

        # 이동 가능한 방향이 나올 때까지 8가지 방향을 체크
        for j in range(8):
            rotated = (direct+j) % 8

            nr, nc = r+directions[rotated][0], c+directions[rotated][1]
            # 이동할 위치가 이동 가능한 위치이면
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != shark:
                # 이동할 칸에 물고기가 있으면
                if new_table[nr][nc][0] > 0:
                    new_table[nr][nc], new_table[r][c] = new_table[r][c], new_table[nr][nc]
                    indices[new_table[nr][nc][0]], indices[new_table[r][c][0]] = indices[new_table[r][c][0]], indices[new_table[nr][nc][0]]
                # 이동할 칸에 물고기가 없으면
                else:
                    new_table[nr][nc] = new_table[r][c][:]
                    new_table[r][c][0] = 0

                # 바뀐 방향으로 갱신
                new_table[nr][nc][1] = rotated
                break 

    return new_table  
    
def dfs(table, shark, ate):
    global results

    table = move_fishes(table, shark)
        
    r, c = shark
    direct = table[r][c][1]
    # 한 칸씩 더 가보는 걸 반복하면서 상어가 이동할 수 있는 경우의 수 탐색
    for i in range(1, 4):
        dr, dc = directions[direct][0], directions[direct][1]
        nr, nc = r + dr*i, c + dc*i
        # 이동하려는 곳이 범위 내 이면서 물고기가 있으면
        if 0 <= nr < 4 and 0 <= nc < 4 and table[nr][nc][0] > 0:
            new_table = [[info[:] for info in line] for line in table]
            new_table[r][c][0] = 0
            dfs(new_table, (nr, nc), ate+new_table[nr][nc][0])

    results.append(ate)

def solution(table):
    shark = (0, 0)
    dfs(table, shark, table[0][0][0])
    return max(results)

def main():
    table = [[(0, 0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(4):
            table[i][j] = [line[j*2], line[j*2+1]-1]

    print(solution(table))

if __name__ == "__main__":
    main()