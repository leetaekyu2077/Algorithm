import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

lst = []
paper = H*W
max = 0

for i in range(0, N):
    R, C = map(int, sys.stdin.readline().split())
    if ((R <= H and C <= W) or 
        (R <= W and C <= H)):
        lst.append([R, C, R*C])

for i, first in enumerate(lst):
    for j, second in enumerate(lst):
        if i != j:
            sum = first[2] + second[2]
            if sum > paper: continue
            if (((first[0] + second[0]) <= H and first[1] <= W and second[1] <= W) or 
                ((first[1] + second[1]) <= H and first[0] <= W and second[0] <= W) or
                ((first[0] + second[1]) <= H and first[1] <= W and second[0] <= W) or 
                ((first[1] + second[0]) <= H and first[0] <= W and second[1] <= W) or
                ((first[0] + second[0]) <= W and first[1] <= H and second[1] <= H) or 
                ((first[1] + second[1]) <= W and first[0] <= H and second[0] <= H) or
                ((first[0] + second[1]) <= W and first[1] <= H and second[0] <= H) or 
                ((first[1] + second[0]) <= W and first[0] <= H and second[1] <= H)) :
                if sum > max: max = sum
print(max)