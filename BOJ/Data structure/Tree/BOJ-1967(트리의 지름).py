import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

p = 0
for _ in range(n-1):
    p, c, w = map(int, input().split()) 
    tree[p].append((c, w))
    tree[c].append((p, w))

def dfs(start):
    max = 0
    idx = 0
    visited = [False]*(n+1)
    visited[start] = True
    stk = [(start, 0)]
    while stk:
        curr = stk.pop()
        if curr[1] > max:
            max = curr[1]
            idx = curr[0]
        visited[curr[0]] = True
        for child in tree[curr[0]]:
            if not visited[child[0]]:
                stk.append((child[0], child[1]+curr[1]))
    
    return idx, max
    
idx, _ = dfs(1)
_, answer = dfs(idx)  
print(answer)