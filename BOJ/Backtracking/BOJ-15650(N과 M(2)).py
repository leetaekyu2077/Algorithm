import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(start, comb, length):
    if length == m:
        print(' '.join(map(str, comb)))
        return 
    else:
        num = start
        while num < n+1:
            if num not in comb:
                comb.append(num)
                dfs(num + 1, comb, length+1)
                comb.pop()
            num += 1           
dfs(1, [], 0)