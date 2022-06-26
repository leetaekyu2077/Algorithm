n = int(input())
m = int(input())

snail = [[0]*n for i in range(n)]
snail[0][0] = n*n
row, col = 0, 0

def fill_snail():
    r, c = 0, 0
    row, col = 0, 0
    while True:
        while snail[r+1][c] == 0:
            snail[r+1][c] = snail[r][c] - 1
            r += 1
            if snail[r][c] == m:
                row, col = r, c
            if snail[r][c] == 1:
                return row, col
            if r == n-1:
                break
        while snail[r][c+1] == 0:
            snail[r][c+1] = snail[r][c] - 1
            c += 1
            if snail[r][c] == m:
                row, col = r, c
            if c == n-1:
                break
        while r > -1 and snail[r-1][c] == 0:
            snail[r-1][c] = snail[r][c] - 1
            r -= 1
            if snail[r][c] == m:
                row, col = r, c
            if r == 0:
                break
        while snail[r][c-1] == 0:
            snail[r][c-1] = snail[r][c] - 1
            c -= 1
            if snail[r][c] == m:
                row, col = r, c
        
row, col = fill_snail()
for i in range(n):
    print(' '.join(map(str, snail[i])))
print(row+1, col+1)