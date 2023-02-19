import sys
input = sys.stdin.readline

def makeNum(i, j, di, dj):
    global all
    si, sj = i, j
    num = nums[si][sj]
    while True:
        si, sj = si+di, sj+dj
        if si < n and -1 < sj < m:
            num += nums[si][sj]
        else:
            break
        
    for k in range(len(num)+1, 0, -1):
        all.add(int(num[:k]))
        all.add(int(num[:k][::-1]))

n, m = map(int, input().split())
nums = [input().rstrip() for _ in range(n)]

all = set([int(nums[0][0])])
for i in range(n):
    for j in range(m):
        for di in range(n):
            for dj in range(-(m-1), m):
                if di or dj:
                    makeNum(i, j, di, dj)

for n in sorted(list(all), reverse=True):
    if int(n**0.5)**2 == n:
        print(n)
        exit(0)
print(-1)