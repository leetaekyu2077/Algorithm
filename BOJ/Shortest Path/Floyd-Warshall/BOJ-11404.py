import sys
input = sys.stdin.readline

def solution(n, graph):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == int(1e9):
                graph[i][j] = 0
    
    for line in graph[1:]:
        print(*line[1:], sep=' ')


def main():
    n = int(input())
    m = int(input())

    graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        s, d, c = map(int, input().split())
        graph[s][d] = min(graph[s][d], c)

    solution(n, graph)

if __name__ == "__main__":
    main()