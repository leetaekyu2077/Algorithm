def solution(lottos, win_nums):
    answer = []
    matched = 0
    possible = 0
    for num in lottos:
        if num in win_nums:
            matched += 1
        elif num == 0:
            possible += 1
    
    # 최고
    if matched == 0 and possible == 0: 
        answer.append(6)
    else:
        answer.append(7 - (matched + possible))  
    # 최저
    if matched == 0 or possible == 6:
        answer.append(6)
    else:
        answer.append(7 - matched)
        
    return answer