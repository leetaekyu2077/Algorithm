import sys
from collections import deque
input = sys.stdin.readline

# def solution(n, k):
#     visited = [False]*100001
#     if n > k:
#         return n-k
    
#     q = deque([n])
#     answer = 0

#     while q:
#         temp = []
#         for curr in q:
#             if curr == k:
#                 return answer

#             visited[curr] = True
#             for x in [curr-1, curr+1, curr*2]:
#                 if 0 <= x < 100001 and not visited[x]:
#                     visited[x] = True
#                     temp.append(x)
        
#         q = deque(temp)
#         answer += 1

def solution(n, k):
    dp = [sys.maxsize] * 200002
    if n > k:
        return n-k
    
    for i in range(n):
        dp[i] = n-i
    
    dp[n] = 0
    for i in range(n, 2*k+1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i-1]+1, dp[i//2]+1)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)
        dp[i-1] = min(dp[i-1], dp[i]+1)

    return dp[k]

def main():
    n, k = map(int, input().split())
    print(solution(n, k))

if __name__ == "__main__":
    main()