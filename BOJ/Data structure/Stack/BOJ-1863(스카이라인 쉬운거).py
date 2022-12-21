import sys

n = int(sys.stdin.readline())
stk = [(0,0)]
answer = 0

skylines = []

for i in range(n):
    skylines.append(tuple(map(int,sys.stdin.readline().split())))

skylines.append((sys.maxsize, 0))
for p in skylines:
    if stk[-1][1] > p[1]:
        answer += 1
        height = stk[-1][1]
        while stk[-1][1] > p[1]:
            if stk[-1][1] != height:
                answer += 1
                height = stk[-1][1]
            stk.pop()
    stk.append(p)
    
print(answer)