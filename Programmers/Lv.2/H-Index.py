def solution(citations):
    answer = 0
    citations.sort()
    
    length = len(citations)
    for i in range(length-1, -1, -1):
        if citations[i] <= answer:
            break
        else:
            answer += 1
    
    return answer