import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(start, dest, costs):
    n = len(costs[0])
    visited = [False]*n
    shortest = [sys.maxsize]*n

    shortest[start] = 0
    adjacent = [(0, start)]

    while adjacent:
        cost, city = heappop(adjacent)
        if visited[city]:
            continue

        # 최소 거리 테이블 업데이트
        visited[city] = True
        for i in range(1, n):
            if costs[city][i] >= 0:
                shortest[i] = min(shortest[i], cost + costs[city][i])
                heappush(adjacent, (shortest[i], i))
    
    return shortest[dest]

def main():
    n = int(input())
    m = int(input())

    costs = [[-1]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        s, d, c = map(int, input().split())
        if costs[s][d] == -1:
            costs[s][d] = c
        else:
            costs[s][d] = min(c, costs[s][d])

    start, dest = map(int, input().split())
    print(solution(start, dest, costs))

if __name__ == "__main__":
    main()