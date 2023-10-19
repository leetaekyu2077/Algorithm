import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def solution(start, n, graph):
    shortest = [int(1e9)]*(n+1)
    visited = [False]*(n+1)

    adjacent = [(0, start)]
    shortest[start] = 0
    while adjacent:
        curr_cost, curr = heappop(adjacent)
        if visited[curr]:
            continue

        visited[curr] = True
        for adj, cost in graph[curr]:
            shortest[adj] = min(shortest[adj], curr_cost+cost)
            heappush(adjacent, (shortest[adj], adj))
    
    for cost in shortest[1:]:
        if cost < int(1e9):
            print(cost)
        else:
            print("INF")


def main():
    v, e = map(int, input().split())
    start = int(input())

    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        s, d, c = map(int, input().split())
        graph[s].append((d, c))

    solution(start, v, graph)

if __name__ == "__main__":
    main()