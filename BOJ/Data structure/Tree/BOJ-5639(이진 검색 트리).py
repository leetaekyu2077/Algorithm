import sys

preorder = []
while True:
    try:
        preorder.append(int(input()))          
    except EOFError:
        break
    
p = preorder[0]
parents = {}
children = {}

parents[p] = 1000001
children[p] = [0]*2

for i in range(1, len(preorder)):
    curr = preorder[i]
    if curr not in children:
        children[curr] = [0]*2
    if curr < p:
        parents[curr] = p
        children[p][0] = curr
    else:
        while parents[p] < curr:
            p = parents[p]
        while children[p][1] != 0:
            p = children[p][1]
        parents[curr] = p
        children[p][1] = curr
    p = curr

sys.setrecursionlimit(20000)  
def postorder(node):
    if node > 0:
        postorder(children[node][0])
        postorder(children[node][1])
        print(node)
        
postorder(preorder[0])