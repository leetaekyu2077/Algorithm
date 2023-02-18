import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

for i in range(k):
    temp = [0]*(n+1)
    for j in range(1, n+1):
        temp[d[j]] = s[j]
    s = temp
    
print(*s[1:])