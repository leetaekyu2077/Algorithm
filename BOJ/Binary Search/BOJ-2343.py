import sys
input = sys.stdin.readline

def solution(lengths, n, m):
    left = max(lengths)
    right = sum(lengths)

    while left <= right:
        mid = (left+right) // 2
        
        count, part = 0, 0
        for i in range(n):
            if part + lengths[i] > mid:
                count += 1
                part = 0
            part += lengths[i]

        if part:
            count += 1

        if count > m:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    
    return answer
        
def main():
    n, m = map(int, input().split())
    lengths = list(map(int, input().split()))

    print(solution(lengths, n, m))

main()