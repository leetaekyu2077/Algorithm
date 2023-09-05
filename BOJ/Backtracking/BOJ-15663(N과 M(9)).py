# import sys

# n, m = map(int, sys.stdin.readline().split())
# nums = sorted(list(map(int, sys.stdin.readline().split())))
# duplicated = dict()
# result = []
# for num in nums:
#     temp = nums.count(num)
#     duplicated[num] = temp
#     while nums.count(num) > 1:
#         nums.remove(num)

# def dfs(comb, length):
#     if length == m:
#         print(' '.join(map(str, comb)))
#         return 
#     else:
#         for num in nums:
#             if duplicated[num] > 0:
#                 duplicated[num] -= 1
#                 comb.append(num)
#                 dfs(comb, length+1)
#                 duplicated[comb.pop()] += 1         
# dfs([], 0)

import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
counts = Counter(nums)

def back_tracking(case):
    if len(case) == m:
        print(*case, sep=' ')
        return

    for n in sorted(list(set(nums))):
        if counts[n]:
            counts[n] -= 1
            back_tracking(case+[n])
            counts[n] += 1

back_tracking([])