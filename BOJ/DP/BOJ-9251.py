import sys
input = sys.stdin.readline

first = input()
second = input()

length = min(len(first), len(second))
lcs = [[0]*(length+1) for _ in range(length+1)]

for i in range(length):
    for j in range(length):
        if first[i] == second[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs)