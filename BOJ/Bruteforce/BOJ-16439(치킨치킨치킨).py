import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
like = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    like.append(temp)

chicken = [i for i in range(m)]
case = combinations(chicken, 3)

max = 0
for entry in case:
    temp_max = 0
    for person in like:
        temp_like = 0
        for c in entry:
            if temp_like < person[c]:
                temp_like = person[c]
        temp_max += temp_like
    if max < temp_max:
        max = temp_max
    
print(max)