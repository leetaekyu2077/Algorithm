from collections import Counter

def solution(gems):
    answer = []

    categories = Counter(gems)
    all = len(categories)
    part = dict()

    left, right = 0, 0
    while right < len(gems):
        # 모든 종류를 포함하지 못했을 때
        if len(part) < all:
            if gems[right] not in part:
                part[gems[right]] = 1
            else:
                part[gems[right]] += 1
        
        # 이미 모든 종류를 포함하고 있을 때
        while len(part) == all:
            answer.append([left+1, right+1])
            # 다음 경우로 넘어가기 위한 처리
            if part[gems[left]] > 1:
                part[gems[left]] -= 1
            else:
                del part[gems[left]]
            left += 1
        right += 1

    if len(part) == all:
        answer.append([left+1, right])

    answer.sort(key = lambda x: ((x[1]-x[0]), x[0]))
    return answer[0]

print(solution(["A","B","B","B","B","B","B","C","B","A"] ))