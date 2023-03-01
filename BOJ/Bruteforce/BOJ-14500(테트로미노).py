import sys
input = sys.stdin.readline

tet1 = [
        [(0, 1), (0, 2), (0, 3)],
        [(1, 0), (2, 0), (3, 0)]
    ]

tet2 = [
        [(0, 1), (1, 1), (1, 0)]
    ]
    
tet3 = [
        [(1, 0), (2, 0), (2, 1)],
        [(0, 1), (0, 2), (1, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 1), (0, 2), (-1, 2)],
        [(0, 1), (-1, 1), (-2, 1)],
        [(1, 0), (1, 1), (1, 2)],
        [(0, 1), (1, 0), (2, 0)],
        [(0, 1), (0, 2), (1, 2)]
    ]
    
tet4 = [
        [(1, 0), (1, 1), (2, 1)],
        [(0, 1), (-1, 1), (-1, 2)],
        [(-1, 0), (-1, 1), (-2, 1)],
        [(0, 1), (1, 1), (1, 2)]
    ]
    
tet5 = [
        [(0, 1), (0, 2), (1, 1)],
        [(0, 1), (-1, 1), (1, 1)],
        [(0, 1), (0, 2), (-1, 1)],
        [(1, 0), (1, 1), (2, 0)]
    ]

def calculate(shape):
    global max
    for i in range(n):
        for j in range(m):
            temp = table[i][j]
            for di, dj in shape:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    temp += table[ni][nj]
                else:
                    break
            
            if temp > max:
                max = temp
            

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

all_cases = [tet1, tet2, tet3, tet4, tet5]

max = 0
for tet in all_cases:
    for shape in tet:
        calculate(shape)

print(max)