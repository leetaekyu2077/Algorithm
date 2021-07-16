import sys

n = int(sys.stdin.readline().rstrip())

for i in range(0, n):
    sentence = list(map(str, sys.stdin.readline().rstrip().split()))

    for word in sentence:
        for i in range(len(word)-1, -1, -1):
            print(word[i], end='')
        print(' ', end='')
    print()