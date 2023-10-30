def solution(nums):
    before = len(nums) // 2
    after = len(set(nums))
    
    if before > after:
        return after
    else:
        return before