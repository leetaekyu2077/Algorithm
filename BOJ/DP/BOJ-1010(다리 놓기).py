import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    p, c = 1, 1
    for i in range(m, m-n, -1):
        p *= i
    for i in range(n, 1, -1):      
        c *= i

    print(p//c)