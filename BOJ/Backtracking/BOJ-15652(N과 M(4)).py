# import sys

# n, m = map(int, sys.stdin.readline().split())

# def dfs(start, comb, length):
#     if length == m:
#         print(' '.join(map(str, comb)))
#         return 
#     else:
#         num = start
#         while num < n+1:
#             comb.append(num)
#             dfs(num, comb, length+1)
#             comb.pop()
#             num += 1           
# dfs(1, [], 0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def back_tracking(case, start):
    if len(case) == m:
        print(' '.join(case))
        return

    for i in range(start, n+1):
        back_tracking(case+[str(i)], i)

back_tracking([], 1)