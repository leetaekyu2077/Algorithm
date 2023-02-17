import sys
from itertools import combinations
input = sys.stdin.readline

# SOL1. PyPy 통과, Python 시간초과 풀이
# n = int(input())
# table = []
# for i in range(n):
#     table.append(list(map(int, input().split())))
  
# answer = sys.maxsize
# for num in range(n//2+1, 1, -1):
#     for team in combinations(range(n), num):
#         other = []
#         for i in range(n):
#             if i not in team:
#                 other.append(i)

#         diff = 0
#         for i in range(1, len(team)):
#             for j in range(i):
#                 diff += table[team[i]][team[j]]
#                 diff += table[team[j]][team[i]]         
            
#         for i in range(1, len(other)):
#             for j in range(i):
#                 diff -= table[other[i]][other[j]]
#                 diff -= table[other[j]][other[i]]   
        
#         if diff == 0:
#             print(diff)
#             exit(0)
            
#         if answer > abs(diff):
#             answer = abs(diff)

# print(answer)

# SOL2. PyPy3, Python 둘다 통과
n = int(input())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
row = [sum(line) for line in stat]
col = [sum(line) for line in zip(*stat)]
stat_sum = [sum(pair) for pair in zip(row, col)]
total_sum = sum(stat_sum) // 2

answer = sys.maxsize
for i in range(1, n):
    for c in combinations(stat_sum[1:], i):
        print(c)
        answer = min(answer, abs(total_sum - sum(c)))
        if answer == 0:
            print(answer)
            exit(0)

print(answer)  