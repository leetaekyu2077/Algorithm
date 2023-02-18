import sys
input = sys.stdin.readline

def solution(nums):
    last = nums[1]
    length = 2
    for num in nums[2:]:
        if nums[0] < last + num:
            length += 1
            last = num
        else:
            break   
    return length
        

n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print(n)
else:
    a.sort(reverse=True)
    answer = 2
    for i in range(n-2):
        if answer > n-i:
            break
        temp = solution(a[i:])
        if answer < temp:
            answer = temp           
    print(answer)   