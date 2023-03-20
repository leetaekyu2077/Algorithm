import sys
input = sys.stdin.readline

records = dict()
records[1] = 0
records[2] = 1

def sol(num):
    if num in records:
        return records[num]
    else:
        records[num] = min(sol(num//3)+num%3, sol(num//2)+num%2)+1
        return records[num]

n = int(input())

# for i in range(1, n+1):
#     nums = [dp[i-1]]    
#     if i%3 == 0:
#         nums.append(dp[i//3])
#     if i%2 == 0:
#         nums.append(dp[i//2])
        
#     dp[i] = min(nums)+1

print(sol(n))