import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def makeTree(node, dep):
    depth[node] = dep
    for i in range(1, max):
        parents[node][i] = parents[parents[node][i-1]][i-1]
    
    for c in child[node]:
        if parents[c][0] == 0:
            parents[c][0] = node
            makeTree(c, dep+1)
        
def lca(a, b):
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a, b = b, a       
        for i in range(max-1, -1, -1):
            if depth[a] <= depth[parents[b][i]]:
                b = parents[b][i]     
                            
    lca = a
    if a != b:
        for i in range(max-1, -1, -1):
            if parents[a][i] != parents[b][i]:
                a = parents[a][i]
                b = parents[b][i]
            lca = parents[a][i]  
    return lca

n = int(input())
depth = [0]*(n+1)

max = int(math.log2(n-1))+1
parents = [[0]*max for _ in range(n+1)]
child = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    child[a].append(b) 
    child[b].append(a)
    
parents[1][0] = 1
makeTree(1, 1)  

m = int(input())
for _ in range(m):
    a, b = map(int, input().split()) 
    print(lca(a, b))