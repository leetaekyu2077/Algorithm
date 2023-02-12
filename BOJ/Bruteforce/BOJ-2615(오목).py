import sys
input = sys.stdin.readline

def check(color, direction, row, col):
    r, c = row, col
    for i in range(6):
        r += next[direction][0]
        c += next[direction][1]
        if r > 18 or c > 18 or r < 0 or c < 0 or board[r][c] != color:
            break
        
    if i == 4:
        row -= next[direction][0]
        col -= next[direction][1]
        if (row > 18 or row < 0 or col < 0 or 
            ((row < 19 or row > -1) and col > -1 and board[row][col] != color)):
            return True
    else:
        return False         

board = []
next = [(-1, 1), (0, 1), (1, 1), (1, 0)]
for _ in range(19):
    board.append(list(map(int, input().split())))
    
for i in range(19):
    for j in range(19):
        if board[i][j] == 1 or board[i][j] == 2:
            curr = board[i][j]
            candidates = []
            if i > 0 and j < 18 and board[i-1][j+1] == curr:
                candidates.append(0)
            if j < 18 and board[i][j+1] == curr:
                candidates.append(1)
            if i < 18 and j < 18 and board[i+1][j+1] == curr:
                candidates.append(2)
            if i < 18 and board[i+1][j] == curr:
                candidates.append(3)

            for c in candidates:
                if check(curr, c, i, j):
                    print(curr)
                    print(i+1, j+1)
                    exit(0)
print(0)                    