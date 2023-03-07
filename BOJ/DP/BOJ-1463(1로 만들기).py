import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)

for i in range(1, n+1):
    nums = [dp[i-1]]    
    if i%3 == 0:
        nums.append(dp[i//3])
    if i%2 == 0:
        nums.append(dp[i//2])
        
    dp[i] = min(nums)+1

print(dp[n]-1)