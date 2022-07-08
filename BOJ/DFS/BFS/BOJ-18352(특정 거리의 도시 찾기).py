import sys
n, m, k, x = map(int, sys.stdin.readline().split())
table = [[] for i in range(n+1)]

for i in range(m):
    r, c = map(int, sys.stdin.readline().split())
    table[r].append(c)
    
q = [(x, 0)]
visited = [0]*(n+1)
result = []

while q:
    current = q.pop(0)
    if current[1] > k: break
    if visited[current[0]] == 0:
        visited[current[0]] = 1 
        if current[1] == k:
            result.append(current[0])
        for city in table[current[0]]:
            q.append((city, current[1]+1))

if result:
    result.sort()
    for item in result: 
        print(item)
else:
    print(-1)