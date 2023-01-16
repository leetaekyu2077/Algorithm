import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(20000)

# 풀이1 - O(N)
# def lca(a, b):
#     ac = {}
#     curr = a
#     while curr > 0:
#         ac[curr] = 0
#         curr = parents[curr]
        
#     curr = b
#     while True:
#         if curr in ac:
#             return curr
#         curr = parents[curr]  

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     parents = [0]*(n+1)
#     for _ in range(n-1):
#         a, b = map(int, input().split())
#         parents[b] = a

#     a, b = map(int, input().split())
#     print(lca(a, b))
# --------------------------------------------------------------

# 풀이2 - LCA 알고리즘 O(logN) 
def makeTree(node, dep):
    depth[node] = dep
    for i in range(1, max):
        parents[node][i] = parents[parents[node][i-1]][i-1]
    
    for c in child[node]:
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

t = int(input())
for _ in range(t):
    n = int(input())
    depth = [0]*(n+1)
    
    max = int(math.log2(n-1))+1
    parents = [[0]*max for _ in range(n+1)]
    child = [[] for _ in range(n+1)]
    
    root = 0
    for _ in range(n-1):
        a, b = map(int, input().split())
        parents[b][0] = a
        child[a].append(b)
        root += b    
    a, b = map(int, input().split())
    
    root = n*(n+1)//2 - root
    makeTree(root, 1)  
    print(lca(a, b))