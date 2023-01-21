import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    classes.append(tuple(map(int, input().split())))
classes.sort()

rooms = [classes[0][1]]
for i in range(1, n):
    if rooms[0] <= classes[i][0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, classes[i][1])

print(len(rooms))