expr = input()

stk = []
answer = []
depth = 0

for c in expr:
    if not stk or c == '(' or c == '[':
        stk.append(c)
        depth += 1
    else:
        if c == ')' and stk[-1] == '(':
            stk.pop()
            depth -= 1
            if not answer or answer[-1][1] < depth:
                answer.append((2, depth))
            elif answer[-1][1] > depth:
                temp = answer.pop()[0] * 2
                if answer and answer[-1][1] == depth:
                    temp += answer.pop()[0]
                answer.append((temp, depth))
            else:
                answer.append((answer.pop()[0] + 2, depth))
        elif c == ']' and stk[-1] == '[':
            stk.pop()
            depth -= 1
            if not answer or answer[-1][1] < depth:
                answer.append((3, depth))
            elif answer[-1][1] > depth:
                temp = answer.pop()[0] * 3
                if answer and answer[-1][1] == depth:
                    temp += answer.pop()[0]
                answer.append((temp, depth))
            else:
                answer.append((answer.pop()[0] + 3, depth))

if stk:
    print(0)
else:
    print(answer[0][0])