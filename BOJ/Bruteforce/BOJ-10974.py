import sys
import copy

n = int(sys.stdin.readline())

init_lst = []

for i in range (1,n+1):
    init_lst.append(i)

def permutation(lst):
    if len(lst) == 1:
        return [lst]
    else:
        result = []
        for i in lst:
            lst_temp = lst.copy()
            lst_temp.remove(i)
            lst_temp.sort()
            #for문 활용 지렸다... 한 수 배워갑니다
            for j in permutation(lst_temp):
                j.insert(0,i)
                result.append(j)
    return result

permutation(init_lst)
res = permutation(init_lst)
for i in res:
    print(' '.join(map(str,i)))