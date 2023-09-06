import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*1001
dp[0] = 1
dp[1] = 3

for i in range(2, n):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[n-1]%10007)