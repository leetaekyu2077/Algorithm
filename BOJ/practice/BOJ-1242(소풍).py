import sys

N, K, M = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, N+1)]
length = N
index = 0
count = 0

for i in range(N):
    index += K-1
    if index >= length:
        index = index % length

    count += 1
    if nums[index] == M:
        print(count)
        exit()
    elif nums[index] > M:
        pass
    elif nums[index] < M:
        M -= 1
    
    length -= 1