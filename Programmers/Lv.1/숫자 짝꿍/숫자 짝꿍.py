def solution(X, Y):
    nums = {}
    common = []
    
    # X를 구성하는 숫자 dict로 정리
    for n in list(X):
        if n in nums:
            nums[n] += 1
        else:
            nums[n] = 1
            
    # Y를 순회하면서 공통 여부 체크
    for n in list(Y):
        if n in nums and nums[n] > 0:
            common.append(n)
            nums[n] -= 1          
            
    if common:
        if common[0] == '0':
            return '0'
        return ''.join(sorted(common, reverse=True))
    else:
        return '-1'