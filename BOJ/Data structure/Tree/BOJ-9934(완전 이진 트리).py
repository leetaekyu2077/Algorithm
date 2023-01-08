import math

K = int(input())
nums = list(map(int, input().split()))
tree = [0]*(int(math.pow(2, K)))

tail = len(nums)
idx = 0

def inorder(node):
    global idx 
    if node <= tail:
        inorder(node*2)
        tree[node] = nums[idx]
        idx += 1
        inorder(node*2+1)

inorder(1)  

tree = list(map(str, tree))
count = 1
for _ in range(K): 
    print(' '.join(tree[count:count*2]))
    count *= 2