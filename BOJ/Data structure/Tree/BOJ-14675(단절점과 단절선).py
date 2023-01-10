import sys
input = sys.stdin.readline

N = int(input())
tree = [0]*(N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a] += 1
    tree[b] += 1
    
q = int(input())
answer = []    

for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if tree[k] > 1:
            answer.append('yes')
        else:
            answer.append('no')
    else:
        answer.append('yes')

print('\n'.join(answer))