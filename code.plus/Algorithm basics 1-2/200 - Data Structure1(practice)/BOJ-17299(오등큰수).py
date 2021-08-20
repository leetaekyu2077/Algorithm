import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count = [0]*10000001
answer = [-1]*N
stack = []

for i in nums:
    count[i] += 1

for i, item in enumerate(nums):
    while stack and count[nums[stack[-1]]] < count[item]:
        answer[stack[-1]] = item
        stack.pop()
    stack.append(i)
print(*answer)