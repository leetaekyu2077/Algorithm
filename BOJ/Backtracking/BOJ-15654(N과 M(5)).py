import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def dfs(comb, length):
    if length == m:
        print(' '.join(map(str, comb)))
        return 
    else:
        for num in nums:
            if num not in comb:
                comb.append(num)
                dfs(comb, length+1)
                comb.pop()          
dfs([], 0)