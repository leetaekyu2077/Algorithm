import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
options = list(permutations('123456789', 3))

for _ in range(n):
    curr, strike, ball = map(lambda x: str(x) if len(x) > 1 else int(x), input().split())
    temp = []
    for num in options:
        s, b = 0, 0
        for j in range(3):
            # 스트라이크 카운트
            if num[j] == curr[j]:
                s += 1
            # 볼 카운트
            elif num[j] in curr:
                b += 1
                
        if s == strike and b == ball:
            temp.append(num)           
    options = temp
print(len(options))