import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
for i in range(1, w-1):
    left = max(heights[:i])
    right = max(heights[i+1:])
    std = min(left, right)
    
    if heights[i] < std:
        answer += std - heights[i]
print(answer)