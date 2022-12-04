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