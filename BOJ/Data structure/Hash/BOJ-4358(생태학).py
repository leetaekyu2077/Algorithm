import sys

trees = dict()
lines = []
total = 0

while True:
    line = sys.stdin.readline().strip()
    if line:
        total += 1
        if line in trees:
            trees[line] += 1
        else:
            trees[line] = 1
    else:
        break

sorted_trees = sorted(trees.items())

for tree in sorted_trees:
    print(f'{tree[0]} {(tree[1]/total)*100:.4f}')