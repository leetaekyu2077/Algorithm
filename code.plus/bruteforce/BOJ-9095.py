import sys

dp = [0]*11

def cut(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if dp[n] == 0:           
            dp[n] = cut(n-1)+cut(n-2)+cut(n-3)
        return dp[n]

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    print(cut(num))