def solution(n, m, section):
    answer = 0
    idx = 0 
    
    while idx < len(section):
        answer += 1
        end = section[idx] + m - 1
        idx += 1
        
        while idx < len(section) and section[idx] <= end:
            idx += 1 
    
    return answer