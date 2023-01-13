import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

preorder = []
while True:
    try:
        preorder.append(int(input()))          
    except:
        break

# 첫 풀이 - Python은 시간초과, PyPy는 통과. but 비효율적임  
# p = preorder[0]
# parents = {}
# children = {}

# parents[p] = 1000001
# children[p] = [0]*2

# for i in range(1, len(preorder)):
#     curr = preorder[i]
#     if curr not in children:
#         children[curr] = [0]*2
#     if curr < p:
#         parents[curr] = p
#         children[p][0] = curr
#     else:
#         while parents[p] < curr:
#             p = parents[p]
#         while children[p][1] != 0:
#             p = children[p][1]
#         parents[curr] = p
#         children[p][1] = curr
#     p = curr

# def postorder(node):
#     if node > 0:
#         postorder(children[node][0])
#         postorder(children[node][1])
#         print(node)
        
# postorder(preorder[0])

# 다시 푼 풀이 - Python으로 통과, 랭킹 풀이 공부
def postorder(start, end):
    if start >= end-1:
        print(preorder[start])
        return
    
    if preorder[start] > preorder[end-1] or preorder[start] < preorder[start+1]:
        postorder(start+1, end)
        print(preorder[start])
        return
    
    mid = 0
    for i in range(start+1, end):
        if preorder[start] < preorder[i]:
            mid = i
            break

    postorder(start+1, mid)
    postorder(mid, end)
    print(preorder[start])
    
postorder(0, len(preorder))