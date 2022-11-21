import sys

expr = sys.stdin.readline().strip()

stk = []
operator = ['+', '-', '*', '/']
answer = ''

for c in expr:
    if c.isalpha():
        answer += c
    else:
        if c == '(':
            stk.append(c)
        elif c == ')':
            while stk:
                temp = stk.pop()
                if temp == '(':
                    break;
                else:
                    answer += temp 
        # 문자열 우선 순위 처리
        else:
            while stk and stk[-1] != '(' and (operator.index(c)//2 <= operator.index(stk[-1])//2):
                temp = stk.pop()
                if temp == '(':
                    break;
                else:
                    answer += temp
            stk.append(c)
    
while stk:
    answer += stk.pop()
    
print(answer)