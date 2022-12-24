import sys, heapq

table = []
heap = []

N = int(sys.stdin.readline())
rows = [N-1]*N

for _ in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    heapq.heappush(heap, (-table[N-1][i], i))

for _ in range(N-1):
    col = heapq.heappop(heap)[1]
    rows[col] -= 1
    heapq.heappush(heap, (-table[rows[col]][col], col))

print(-heap[0][0])