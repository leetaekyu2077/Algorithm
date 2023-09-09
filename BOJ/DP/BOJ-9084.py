import sys
input = sys.stdin.readline

def solution(n, coins, m):
    # dp 테이블 초기화
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j-coins[i] >= 0:
                dp[i][j] += dp[i][j-coins[i]]
    
    return dp[n][m]

def main():
    t = int(input())
    for _ in range(t):
        coins = [0]
        n = int(input())
        coins.extend(list(map(int, input().split())))
        m = int(input())
        
        print(solution(n, coins, m))

if __name__ == "__main__":
    main()