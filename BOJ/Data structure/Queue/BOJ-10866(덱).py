import sys
from typing import Deque

n = int(sys.stdin.readline())
front_stack = list()
back_stack = list()
f_length = 0
b_length = 0

for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_front':
        front_stack.append(cmd[1])
        f_length += 1
    elif cmd[0] == 'push_back':
        back_stack.append(cmd[1])
        b_length += 1
    elif cmd[0] == 'size':
        print(f_length + b_length)
    elif cmd[0] == 'empty':
        if (f_length + b_length) > 0:
            print(0)
        else:
            print(1)
    elif f_length + b_length == 0:
        print(-1)
    elif cmd[0] == 'pop_front':
        if f_length > 0:
            print(front_stack.pop())
            f_length -= 1
        else:
            print(back_stack.pop(0))
            b_length -= 1
    elif cmd[0] == 'pop_back':
        if b_length > 0:
            print(back_stack.pop())
            b_length -= 1
        else: 
            print(front_stack.pop(0))
            f_length -= 1
    elif cmd[0] == 'front':
        if f_length > 0:
            print(front_stack[f_length-1])
        else:
            print(back_stack[0])
    elif cmd[0] == 'back':
        if b_length > 0:
            print(back_stack[b_length-1])
        else: 
            print(front_stack[0])


    
