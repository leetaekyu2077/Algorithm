import sys

n = int(sys.stdin.readline().rstrip())
answer = []
stack = []
result = ''

for i in range(0, n):
    answer.append(int(sys.stdin.readline().rstrip()))

stack.append(1)
result += '+'
iter = 2
flag = False

while flag is False:
    if len(stack) > 0 and stack[len(stack)-1] == answer[0]:
        stack.pop()
        answer.pop(0)
        result += '-'
    elif iter <= n:
        stack.append(iter)
        iter = iter + 1
        result += '+'
    else:
        flag = True

if len(answer) == 0:
    for i in range(0, len(result)):
        print(result[i])
else:
    print('NO')

