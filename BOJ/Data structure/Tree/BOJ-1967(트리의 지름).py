import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n = int(input())
from_root = [0]*(n+1)
parents = [0]*(n+1)
tree = [[] for _ in range(n+1)]

p = 0
for _ in range(n-1):
    p, c, w = map(int, input().split()) 
    tree[p].append((c, w))
    
q = deque([1])
while q:
    curr = q.popleft()
    for c, w in tree[curr]:
        if parents[c] == 0:
            parents[c] = curr
            from_root[c] = from_root[curr] + w
            q.append(c)
  
leaves = [i for i in range(p+1, n+1)]  
if len(tree[1]) > 0 and len(tree[1]) < 2:
    leaves.append(1)
    
max = 0
for case in combinations(leaves, 2):
    p1 = []
    lcp = case[0]
    while lcp > 1:
        p1.append(parents[lcp])
        lcp = parents[lcp]
    lcp = case[1]
    while lcp not in p1:
        lcp = parents[lcp]
    
    dist = from_root[case[0]] + from_root[case[1]] - 2*from_root[lcp]
    if max < dist:
        max = dist
        
print(max)