import sys

#커서를 기준으로 문자를 각각 왼쪽, 오른쪽 스택에 분할하여
#커서 이동 or 삽입 or 삭제 연산에서 각 스택의 끝에 있는 요소를 수정함으로써
#시간 복잡도를 줄이는 방법 
#https://suri78.tistory.com/112 참고

left_stack = list(sys.stdin.readline().rstrip())
right_stack = list()
n = int(sys.stdin.readline().strip())

for i in range(n):
    cmd = sys.stdin.readline()
    if cmd[0] == 'L' and left_stack:
        right_stack.append(left_stack.pop())
    elif cmd[0] == 'D' and right_stack:
        left_stack.append(right_stack.pop())
    elif cmd[0] == 'B' and left_stack:
        left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[2])

#오른쪽 스택은 거꾸로 출력
sys.stdout.write(''.join(left_stack + right_stack[::-1]))