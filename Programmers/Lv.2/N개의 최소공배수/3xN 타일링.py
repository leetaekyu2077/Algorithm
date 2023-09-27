def solution(n):
    
    dp = [0]*5001
    dp[2] = 3
    
    for i in range(4, n+1, 2):
        dp[i] = (dp[i-2]*3 + sum(dp[2:i-3:2])*2 + 2) % 1000000007
    
    return dp[n]