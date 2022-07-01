import sys

N, K = map(int, sys.stdin.readline().split())

nums = [str(i) for i in range(1, N+1)]
result = list()
length = N
index = 0

for i in range(N):
    index += K-1
    if index >= length:
        index = index % length

    result.append(nums.pop(index))
    length -= 1

print('<', ', '.join(result), '>', sep='')
