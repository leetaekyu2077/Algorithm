import sys
input = sys.stdin.readline

n = int(input())
time = []
answer = 1

for i in range(n):
    time.append(tuple(map(int, input().split())))
    
time.sort(key=lambda x:(x[1], x[0]))
last = time[0]

for i in range(1, n):   
    if time[i][0] >= last[1]:
        last = time[i]
        answer += 1

print(answer)