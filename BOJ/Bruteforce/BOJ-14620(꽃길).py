import sys
from itertools import combinations
input = sys.stdin.readline

def check(case):
    used = []
    for r, c in case:
        mid = r*n+c
        need = [mid, mid+n, mid-n, mid+1, mid-1]
        for p in need:
            if p in used:
                return False
        used.extend(need)  
    
    return True 

def calc(case):
    result = 0
    for r, c in case:
        result += garden[r][c]
        result += garden[r+1][c]
        result += garden[r-1][c]
        result += garden[r][c+1]
        result += garden[r][c-1]   
        
    return result

n = int(input())
garden = []

for _ in range(n):
    garden.append(list(map(int, input().split())))

min = sys.maxsize
positions = []
for i in range(1, n-1):
    for j in range(1, n-1):
        positions.append((i, j))
        
for case in combinations(positions, 3):
    if check(case):
        cost = calc(case)
        if min > cost:
            min = cost

print(min)