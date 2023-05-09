import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
results = defaultdict(int)

for _ in range(n):
    _, extender = input().split('.')
    results[extender.rstrip()] += 1

print('\n'.join(key+' '+str(results[key]) for key in sorted(results.keys())))