import sys

N = int(sys.stdin.readline())
circles = []

for i in range(N):
    x, r = map(int, sys.stdin.readline().split());
    circles.append((x-r, i))
    circles.append((x+r, i))    
circles.sort()
print(circles)

# 올바른 괄호인지 판단하는 문제를 풀 때와 비슷. 그러나 짝이 정해져 있는 괄호라고 생각하고 풀어야 함
# 원의 왼쪽 끝이 자신의 오른쪽 끝을 연속해서 만날 때만 짝지어져 제거 됨.
# 중간에 다른 원의 시작점이 끼어든 후 제거되지 않으면(두 원이 서로 겹치면) 자신의 원의 끝점과 짝지어지지 못해 제거되지 않음

stk = []
for c in circles:
    if stk:
        if stk[-1][1] == c[1]:
            stk.pop()
        else:
            stk.append(c)
    else:
        stk.append(c) 
    
if stk:
    print('NO')
else:
    print('YES')