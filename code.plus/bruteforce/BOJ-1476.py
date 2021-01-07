import sys

E, S, M = map(int, sys.stdin.readline().split())
E = E%15
S = S%28
M = M%19
year = 1

while True:
    if year%15 == E and year%28 == S and year%19 == M:
        break
    else:
        year += 1

print(year)