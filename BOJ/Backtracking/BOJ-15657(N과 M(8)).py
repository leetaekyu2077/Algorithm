import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def dfs(num, comb, length):
    if length == m:
        print(' '.join(map(str, comb)))
        return 
    else:
        for i in range(num, len(nums)):
            comb.append(nums[i])
            dfs(i, comb, length+1)
            comb.pop()          
dfs(0, [], 0)