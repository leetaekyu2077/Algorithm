import sys
from itertools import combinations
input = sys.stdin.readline

def countOdds(curr):
    cnt = 0
    for num in curr:
        if int(num) % 2 == 1:
            cnt += 1   
    return cnt

def operate(curr, odd):
    new_num = ''
    odd += countOdds(curr)
    if len(curr) == 1:
        results.append(odd)
    elif len(curr) == 2:
        new_num = str(int(curr[0])+int(curr[1]))
        operate(new_num, odd)
    else:
        for case in combinations(range(1, len(curr)), 2):
            new_num = str(int(curr[:case[0]]) + int(curr[case[0]:case[1]]) + int(curr[case[1]:]))
            operate(new_num, odd)

n = input().rstrip()
results = []  
operate(n, 0)

print(min(results), max(results))   