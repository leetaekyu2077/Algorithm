import sys
input = sys.stdin.readline

def add():
    global curr, lst
    for i in range(len(curr)-1, -1, -1):
        for j in range(len(lst)):
            if curr[i][1] < lst[j][1]:
                curr.insert(i+1, lst.pop(j))
                result.append(toString(curr))
                return
    
    curr.insert(i, lst.pop(0))
    result.append(toString(curr))
    
def toString(arr):
    return ''.join([c for c, _ in arr])

s = input().rstrip()
lst = [(s[i], i) for i in range(len(s))]
lst.sort()

length = len(s)
curr = [lst[0]]
result = [lst[0][0]]
cnt = 1
lst.pop(0)

while cnt < length:
    cnt += 1
    add()
    
print(*result, sep='\n')