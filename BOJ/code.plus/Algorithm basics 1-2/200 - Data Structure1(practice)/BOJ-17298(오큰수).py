import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
answer = [-1]*N
stack = []

answer[N-1] = -1
# for i, v in enumerate(list): 형태는
# i는 인덱스 값, v는 그 위치의 요소값을 가진 tuple 형태 반환
for i, item in enumerate(nums):
    while (stack and nums[stack[-1]] < item):
        answer[stack[-1]] = item
        stack.pop()
    stack.append(i)
print(*answer)