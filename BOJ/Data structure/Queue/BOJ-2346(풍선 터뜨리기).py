import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

ballons = deque(enumerate(map(int, input().split()), start=1))
answer = []

while ballons:
    now, next = ballons.popleft()
    answer.append(now)
    if next > 0:
        ballons.rotate(-(next-1))
    else:
        ballons.rotate(-next)     
    
print(' '.join(map(str, answer))) 