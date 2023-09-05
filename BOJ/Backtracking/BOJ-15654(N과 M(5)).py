# import sys

# n, m = map(int, sys.stdin.readline().split())
# nums = sorted(list(map(int, sys.stdin.readline().split())))


# def dfs(comb, length):
#     if length == m:
#         print(' '.join(map(str, comb)))
#         return 
#     else:
#         for num in nums:
#             if num not in comb:
#                 comb.append(num)
#                 dfs(comb, length+1)
#                 comb.pop()          
# dfs([], 0)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def back_tracking(case):
    if len(case) == m:
        print(*case, sep=' ')
        return

    for n in nums:
        if n not in case:
            back_tracking(case+[n])

back_tracking([])