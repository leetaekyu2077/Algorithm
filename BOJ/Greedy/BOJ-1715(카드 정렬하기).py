import sys
import heapq

n = int(sys.stdin.readline())
bundles = []
combined = 0
result = 0
for i in range(n):
    temp = int(sys.stdin.readline())
    heapq.heappush(bundles, temp)

while len(bundles) > 1:
    combined = heapq.heappop(bundles) + heapq.heappop(bundles)
    heapq.heappush(bundles, combined)
    result += combined
print(result)