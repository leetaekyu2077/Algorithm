import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global visited
    q = deque([start])
    cnt = -1
    
    while q:
        cnt += 1 
        cycle = q.copy()            
        q.clear()
        while cycle:
            curr = cycle.popleft()      
            if ''.join(curr) == target:
                return cnt
            
            empty = curr.index('0')
            
            if (empty // 3) > 0:
                temp = curr[:]
                temp[empty], temp[empty-3] = temp[empty-3], '0'
                temp_str = ''.join(temp)
                if temp_str not in visited:
                    visited[temp_str] = True
                    q.append(temp)
                
            if (empty % 3) < 2:
                temp = curr[:]
                temp[empty], temp[empty+1] = temp[empty+1], '0'
                temp_str = ''.join(temp)
                if temp_str not in visited:
                    visited[temp_str] = True
                    q.append(temp)
                    
            if (empty // 3) < 2:
                temp = curr[:]
                temp[empty], temp[empty+3] = temp[empty+3], '0'
                temp_str = ''.join(temp)
                if temp_str not in visited:
                    visited[temp_str] = True
                    q.append(temp)
                    
            if (empty % 3) > 0:
                temp = curr[:]
                temp[empty], temp[empty-1] = temp[empty-1], '0'
                temp_str = ''.join(temp)
                if temp_str not in visited:
                    visited[temp_str] = True
                    q.append(temp)   

start = []
for _ in range(3):
    start.extend(list(input().split()))
    
visited = dict()
target = '123456780'

result = bfs(start)
if result == None:
    print(-1)
else:
    print(result)