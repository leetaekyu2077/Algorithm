import sys
from collections import defaultdict
input = sys.stdin

n = int(input.readline())
temp = list(map(int, input.readline().split()))
numbers = defaultdict(int)
for num in temp:
    numbers[num] = 1
    
m = int(input.readline())
targets = list(map(int, input.readline().split()))

for t in targets:
    print(1 if numbers.get(t) != None else 0)
        