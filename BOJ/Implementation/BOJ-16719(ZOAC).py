import sys
input = sys.stdin.readline

# 1등 풀이 참조
def solution(curr, start):
    global state
    if not curr:
        return
    c = min(curr)
    idx = curr.index(c)
    state[start+idx] = c
    print(''.join(state))
    
    solution(curr[idx+1:], start+idx+1)
    solution(curr[:idx], start)

s = list(input().rstrip())
state = ['']*len(s)
solution(s, 0)

# 최초 풀이
# def add():
#     global curr, lst
#     for i in range(len(curr)-1, -1, -1):
#         for j in range(len(lst)):
#             if curr[i][1] < lst[j][1]:
#                 curr.insert(i+1, lst.pop(j))
#                 result.append(toString(curr))
#                 return
    
#     curr.insert(i, lst.pop(0))
#     result.append(toString(curr))
    
# def toString(arr):
#     return ''.join([c for c, _ in arr])

# s = input().rstrip()
# lst = [(s[i], i) for i in range(len(s))]
# lst.sort()

# length = len(s)
# curr = [lst[0]]
# result = [lst[0][0]]
# cnt = 1
# lst.pop(0)

# while cnt < length:
#     cnt += 1
#     add()
    
# print(*result, sep='\n')