import sys
input = sys.stdin.readline

n = int(input())

stairs = [0]*300
for i in range(n):
    stairs[i] = int(input())

dp = [0]*300
dp[0] = stairs[0]
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[n-1])

# dp = [[[0, 0] for _ in range(2)] for _ in range(301)]
# dp[0][0] = [stairs[0], 1]

# if n > 1:
#     dp[1][0] = [stairs[0]+stairs[1], 2]
#     dp[1][1] = [stairs[1], 1]

# count = 1
# for i in range(2, len(stairs)):
#     if dp[i-1][0][1] < 2:
#         if dp[i-1][0][0] > dp[i-1][1][0]:
#             dp[i][0] = [dp[i-1][0][0]+stairs[i], dp[i-1][0][1]+1]
#         else:
#             dp[i][0] = [dp[i-1][1][0]+stairs[i], dp[i-1][1][1]+1]
#     else: 
#         dp[i][0] = [dp[i-1][1][0]+stairs[i], dp[i-1][1][1]+1]

#     if dp[i-2][0][0] > dp[i-2][1][0]:
#             dp[i][1] = [dp[i-2][0][0]+stairs[i], 1]
#     else:
#         dp[i][1] = [dp[i-2][1][0]+stairs[i], 1]

# print(max(dp[n-1][0][0], dp[n-1][1][0]))