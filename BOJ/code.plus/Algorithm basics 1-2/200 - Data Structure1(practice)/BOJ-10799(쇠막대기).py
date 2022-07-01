import sys

S = sys.stdin.readline().rstrip()

answer = 0
length = len(S)
stack_len = 0

for i in range(length):
    if S[i] == '(':
        stack_len += 1
    elif S[i] == ')':
        stack_len -= 1
        if S[i-1] == '(':
            answer += stack_len
        else:
            answer += 1
print(answer)