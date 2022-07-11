import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(comb, length):
    if length == m:
        print(' '.join(map(str, comb)))
        return 
    else:
        num = 1
        while num < n+1:
            comb.append(num)
            dfs(comb, length+1)
            comb.pop()
            num += 1           
dfs([], 0)