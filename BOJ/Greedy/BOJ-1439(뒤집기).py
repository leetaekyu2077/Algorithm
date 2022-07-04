import sys

S = list(map(int, sys.stdin.readline().strip()))

std = 2
zero = 0
one = 0
for i in range(len(S)):
    if S[i] != std:
        std = S[i]
        if S[i] == 0: zero += 1
        if S[i] == 1: one += 1
print(min(zero, one))