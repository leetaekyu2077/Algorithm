import sys
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1
while a < b:
    if b % 2 == 0:
        b //= 2
    else:
        if b % 10 == 1:
            b //= 10
        else:
         break
    count += 1

print(count if a == b else -1)