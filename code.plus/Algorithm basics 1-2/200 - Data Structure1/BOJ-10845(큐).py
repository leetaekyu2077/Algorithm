import sys

n = int(sys.stdin.readline()[:-1])
queue = list()
length = 0

for i in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push':
        queue.append(cmd[1])
        length += 1
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if length > 0:
            print(0)
        else:
            print(1)
    elif length == 0:
        print(-1)
    elif cmd[0] == 'pop':
        length -= 1
        print(queue.pop(0))
    elif cmd[0] == 'front':
        print(queue[0])
    elif cmd[0] == 'back':
        print(queue[length-1])


