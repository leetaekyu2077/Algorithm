import sys
input = sys.stdin.readline

def solution(perm):
    visited = [False]*(n+1)
    cycle = 0
    
    for i in range(1, n+1):
        idx, curr = i, perm[i]
        if not visited[i]:
            cycle += 1
            while perm[curr] != perm[i]:
                visited[curr] = True
                idx = curr
                curr = perm[curr]
    
    return cycle
                
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0]
    nums.extend(list(map(int, input().split())))
    print(solution(nums))
    