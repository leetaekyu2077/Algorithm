import sys
input = sys.stdin.readline

def solution(stuffs, n, k):

    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            # 새 물건을 넣지 못함
            if stuffs[i][0] > j:
                dp[i][j] = dp[i-1][j]
            # 새 물건을 넣음 (안 넣고 넘어가는 것, 이전 물건을 빼고 현재 물건을 넣는 것 중 가치가 큰 것을 결정)
            else:
                if j-stuffs[i][0] >= 0:
                    temp = stuffs[i][1] + dp[i-1][j-stuffs[i][0]]
                else:
                    temp = stuffs[i][1]
                dp[i][j] = max(dp[i-1][j], temp)

    return dp[n][k]

def main():
    n, k = map(int, input().split())
    stuffs = [0]*(n+1)

    for i in range(1, n+1):
        w, v = map(int, input().split())
        stuffs[i] = (w, v)

    print(solution(stuffs, n, k))

main()