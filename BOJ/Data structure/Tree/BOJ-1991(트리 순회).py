import sys
input = sys.stdin.readline

N = int(input())

tree = dict()

for _ in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)
  
answer = ''
    
def preorder(node):
    global answer
    
    if node in tree:
        l, r = tree[node]
        answer += node
        preorder(l)
        preorder(r)
    
    

def inorder(node):
    global answer
    
    if node in tree:
        l, r = tree[node]
        inorder(l)
        answer += node
        inorder(r)


def postorder(node):
    global answer
      
    if node in tree:
        l, r = tree[node]
        postorder(l)
        postorder(r)
        answer += node

preorder('A')
answer += '\n'
inorder('A')
answer += '\n'
postorder('A')

print(answer)