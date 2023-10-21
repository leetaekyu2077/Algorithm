def solution(m, n, puddles):
    dp = [[1]*m for _ in range(n)]
    
    for pc, pr in puddles:
        dp[pr-1][pc-1] = 0
        
        if pc == 1:
            for i in range(pr, n):
                dp[i][0] = 0
        
        if pr == 1:
            for i in range(pc, m):
                dp[0][i] = 0
        
    for i in range(1, n):
        for j in range(m-1):
            if dp[i][j+1] != 0:
                dp[i][j+1] = (dp[i][j] + dp[i-1][j+1]) % 1000000007            
    
    return dp[n-1][m-1]