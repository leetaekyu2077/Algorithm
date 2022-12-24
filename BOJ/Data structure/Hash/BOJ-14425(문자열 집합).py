import sys

N, M = map(int, sys.stdin.readline().split())

S = {}
answer = 0

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    S[line] = True

for _ in range(M):
    line = sys.stdin.readline().rstrip()
    if line not in S:
        pass
    else:
        answer += 1

print(answer)