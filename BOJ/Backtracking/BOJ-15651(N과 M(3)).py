# import sys

# n, m = map(int, sys.stdin.readline().split())

# def dfs(comb, length):
#     if length == m:
#         print(' '.join(map(str, comb)))
#         return 
#     else:
#         num = 1
#         while num < n+1:
#             comb.append(num)
#             dfs(comb, length+1)
#             comb.pop()
#             num += 1           
# dfs([], 0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def back_tracking(case):
    if len(case) == m:
        print(' '.join(case))
        return

    for i in range(1, n+1):
        back_tracking(case+[str(i)])

back_tracking([])