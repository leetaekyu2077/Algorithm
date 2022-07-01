def solution(numbers, hand):
    answer = ''
    left = 9
    right = 11
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = num - 1
        if num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = num - 1
        if num == 2 or num == 5 or num == 8 or num == 0:
            # 각 위치를 2차원 배열 인덱스로 위치 표현하여 거리 계산
            # 0일 때는 계산 통일을 위해 11로 계산
            if num == 0: num = 11
            dist_l = abs(left//3-(num-1)//3)+abs(left%3-(num-1)%3)
            dist_r = abs(right//3-(num-1)//3)+abs(right%3-(num-1)%3)
            if dist_l > dist_r:
                answer += 'R'
                right = num - 1
            elif dist_l < dist_r:
                answer += 'L'
                left = num - 1
            else:
                if hand[0] == 'r':
                    answer += 'R'
                    right = num - 1
                else:
                    answer += 'L'
                    left = num - 1        
    return answer