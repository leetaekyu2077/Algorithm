import sys

S = list(sys.stdin.readline().strip())

length = len(S)
start = 0
i = 0
tag = False
answer = ''

while i < length:
    if S[i] == '<':
        start = i
        i += 1
        while S[i] != '>':
            i += 1
        i += 1
    elif S[i].isalnum():
        start = i
        while i < length and S[i].isalnum():
            i += 1
        if start == 0:
            S[start:i] = S[i-1::-1]
        else:
            S[start:i] = S[i-1:start-1:-1]
    else:
        i += 1

print("".join(S))