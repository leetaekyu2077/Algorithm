import sys

n = int(sys.stdin.readline())
drinks = list(map(int, sys.stdin.readline().split()))

drinks.sort()
max = drinks.pop()  

while len(drinks) > 0:
    max += drinks.pop() / 2
print(max)