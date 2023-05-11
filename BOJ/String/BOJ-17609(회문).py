import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    
    err_cnt = 0
    left, right = 0, len(s)-1
    
    while left < right and err_cnt < 2:
        if s[left] == s[right]:
            left += 1
            right -= 1  
        else:
            err_cnt += 1
            if left +1 == right:
                break
            if left+1 < right:
                temp = s[left+1:right+1] 
                if temp == temp[::-1]:
                    break
            if left < right-1:
                temp = s[left:right] 
                if temp == temp[::-1]:
                    break
    print(err_cnt)