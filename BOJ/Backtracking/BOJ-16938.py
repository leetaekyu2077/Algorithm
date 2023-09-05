import sys
from itertools import combinations
input = sys.stdin.readline

n, l, r, x = map(int, input().split())
diffs = list(map(int, input().split()))
answer = 0

def check(case):
    return ((l <= sum(case) <= r) and 
            (max(case) - min(case)) >= x)

all = []
for i in range(2, n+1):
    for case in combinations(diffs, i):
        if check(case):
            answer += 1

print(answer)