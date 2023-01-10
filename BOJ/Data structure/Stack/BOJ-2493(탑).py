# 뒤에서부터 역순으로
from sys import stdin

N = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
stk = [(N-1, towers[N-1])]
answers = ['0'] * N

for i in range(N-2, -1, -1):
    while stk and towers[i] >= stk[-1][1]:
        temp = stk.pop()
        answers[temp[0]] = str(i+1)
    stk.append((i, towers[i]))

print(" ".join(answers))

# 앞에서부터 차례대로
# from sys import stdin

# N = int(stdin.readline())
# towers = list(map(int, stdin.readline().split()))
# answers = ['0'] * N
# stk = []

# for i in range(N):
#     while stk:
#         if towers[i] > stk[-1][1]:
#             stk.pop()
#         else:
#             answers[i] = str(stk[-1][0]+1)
#             break
        
#     stk.append((i, towers[i]))

# print(" ".join(answers))