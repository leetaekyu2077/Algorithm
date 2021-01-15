import sys

n = int(sys.stdin.readline())

lst = list(map(int,sys.stdin.readline().split()))

def get_next(lst):
    if n == 1:
        return [-1]
    for i in range(n-1, 0, -1):
        if lst[i] < lst[i-1]:
            break
    if i == 1 and lst[0] < lst[1]:
        return [-1]
    
    for j in range(n-1,i-1,-1):
        if lst[i-1] > lst[j]:
            break
    
    lst[i-1],lst[j] = lst[j],lst[i-1]
    lst_tmp = lst[i:]
    lst_tmp.reverse()
    lst = lst[0:i] + lst_tmp
    return lst

lst = get_next(lst)
lst = [str(i) for i in lst]
print(' '.join(lst))

    