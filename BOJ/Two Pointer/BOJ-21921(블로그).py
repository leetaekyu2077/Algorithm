import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

visited_sum = [0]*(n-x+1)
visited_sum[0] = sum(visitors[0:x])

for i in range(0, n-x):
    visited_sum[i+1] = visited_sum[i] - visitors[i] + visitors[x+i]

max_visitor = max(visited_sum)
if not max_visitor:
    print("SAD")
else:
    print(max_visitor)
    print(visited_sum.count(max_visitor))