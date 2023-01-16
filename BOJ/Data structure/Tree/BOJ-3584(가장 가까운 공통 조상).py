import sys
input = sys.stdin.readline

def lca(a, b):
    ac = {}
    curr = a
    while curr > 0:
        ac[curr] = 0
        curr = parents[curr]
        
    curr = b
    while True:
        if curr in ac:
            return curr
        curr = parents[curr]  

t = int(input())
for _ in range(t):
    n = int(input())
    parents = [0]*(n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parents[b] = a

    a, b = map(int, input().split())
    print(lca(a, b))