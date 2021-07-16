import sys

x = int(sys.stdin.readline().rstrip()) #input보다 입력속도 현저히 빠름@@@@
stack = []
command = []

for i in range(0, x):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if len(stack) > 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop(len(stack)-1))
        else:
            print(-1)
