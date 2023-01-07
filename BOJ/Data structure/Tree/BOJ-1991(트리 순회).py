import sys
input = sys.stdin.readline

N = int(input())

tree = dict()

for _ in range(N):
    p, l, r = input().split()
    tree[p] = (l, r)
    
def preorder(node):
    if node in tree:
        l, r = tree[node]
        print(node, end='')
        preorder(l)
        preorder(r)  

def inorder(node):
    if node in tree:
        l, r = tree[node]
        inorder(l)
        print(node, end='')
        inorder(r)

def postorder(node):
    if node in tree:
        l, r = tree[node]
        postorder(l)
        postorder(r)
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')