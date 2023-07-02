import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
lst_n = list(map(int, input().split()))
lst_m = list(map(int, input().split()))

idx_n, idx_m = 0, 0
result = []
while True:
    if lst_n[idx_n] <= lst_m[idx_m]:
        result.append(lst_n[idx_n])
        idx_n += 1
        if idx_n == n: 
            result.extend(lst_m[idx_m:])
            break
    else:
        result.append(lst_m[idx_m])
        idx_m += 1
        if idx_m == m: 
            result.extend(lst_n[idx_n:])
            break

print(*result, sep=" ")