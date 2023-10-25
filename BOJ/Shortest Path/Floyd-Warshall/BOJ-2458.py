import sys
input = sys.stdin.readline


def solution(n, graph):
    answer = 0

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    for a in range(1, n+1):
        cnt = 0
        for i in range(1, n+1):
            if graph[a][i] < int(1e9): cnt += 1
            if graph[i][a] < int(1e9): cnt += 1

        if cnt == n-1:
            answer += 1

    return answer


def main():
    n, m = map(int, input().split())

    graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    print(solution(n, graph))
    

if __name__ == "__main__":
    main()