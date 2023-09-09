import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    print(bisect_right(cards, t)-bisect_left(cards, t), end=' ') 