import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

diff = [0]*(n-1)
for i in range(n-1):
    diff[i] = heights[i+1]-heights[i]
  
diff.sort()  
for _ in range(k-1):
    diff.pop()
    
print(sum(diff))