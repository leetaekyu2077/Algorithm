import sys
input = sys.stdin.readline

def solution(lans, max, n):
    left = 1
    right = max

    while left <= right:
        mid = (left+right)//2
        parts = 0
        
        for each in lans:
            parts += each // mid
    
        if n <= parts: 
            left = mid+1
        else: 
            right = mid-1

    return right

def main():
    k, n = map(int, input().split())
    lans = []
    for _ in range(k):
        lans.append(int(input()))
    
    print(solution(lans, max(lans), n))

main()