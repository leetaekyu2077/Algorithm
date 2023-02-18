import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

def dfs(t):
    if t == s:
        print(1)
        exit(0)
    elif len(t) == 0:
        return
    if t[0] == 'B':
        dfs(t[1:][::-1])
    if t[-1] == 'A':
        dfs(t[:-1])

dfs(t)
print(0)