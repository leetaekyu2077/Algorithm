from sys import stdin

answers = []

def remove_parenthesis(expr):
    stk = []
    for i in range(len(expr)):
        if expr[i] == '(':
            stk.append(i)
        elif expr[i] == ')':
            temp = expr[:]
            del temp[i]
            del temp[stk.pop()]
            temp_str = "".join(temp)
            if temp_str not in answers:
                answers.append(temp_str)
                remove_parenthesis(temp)

remove_parenthesis(list(stdin.readline().rstrip()))
answers.sort()
for answer in answers:
    print(answer)