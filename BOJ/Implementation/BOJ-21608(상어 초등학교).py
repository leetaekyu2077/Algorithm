import sys
input = sys.stdin.readline

# 1번 규칙 체크, 결정 안되면 후보들을 가지고 2번 규칙으로
def rule1(like):   
    candidates = set()
    new_candidates = []
    
    # 자리가 정해진 학생 중에 좋아하는 학생이 있다면, 그와 인접한 자리들을 우선 후보로
    for num in like:
        if seats[num]:
            r, c = seats[num]
            if r > 1 and room[r-1][c] == 0:
                candidates.add((r-1, c))
            if c < n and room[r][c+1] == 0:
                candidates.add((r, c+1))
            if r < n and room[r+1][c] == 0:
                candidates.add((r+1, c))
            if c > 1 and room[r][c-1] == 0:
                candidates.add((r, c-1))

    # 자리가 정해진 학생 중 좋아하는 학생이 있을 때,
    if candidates:
        candidates = list(candidates)
        score = [0]*len(candidates)
        for i in range(len(candidates)):
            r, c = candidates[i]
            if r > 1 and room[r-1][c] in like:
                score[i] += 1
            if c < n and room[r][c+1] in like:
                score[i] += 1
            if r < n and room[r+1][c] in like:
                score[i] += 1
            if c > 1 and room[r][c-1] in like:
                score[i] += 1
        
        highest = max(score)
        for i in range(len(score)):
            if score[i] == highest:
                new_candidates.append(candidates[i])
        
        if len(new_candidates) == 1:
            return new_candidates[0]
        else:
            new_candidates.sort()
    
    # 자리가 정해진 학생 중 좋아하는 학생이 없을 때,
    else:
        for r in range(1, n+1):
            for c in range(1, n+1):
                if room[r][c] == 0:
                    new_candidates.append((r, c))
        
    return rule2(new_candidates)

# 2번 규칙 체크, 결정 안되면 후보들을 가지고 3번 규칙으로
def rule2(candidates):
    score = [0]*len(candidates)
    for i in range(len(candidates)):
        r, c = candidates[i]
        if r > 1 and room[r-1][c] == 0:
            score[i] += 1
        if c < n and room[r][c+1] == 0:
            score[i] += 1
        if r < n and room[r+1][c] == 0:
            score[i] += 1
        if c > 1 and room[r][c-1] == 0:
            score[i] += 1
    
    # rule3 - 규칙 3
    highest = max(score)
    for i in range(len(score)):
        if score[i] == highest:
            return candidates[i]      


n = int(input())
room = [[0]*(n+1) for _ in range(n+1)]
students = []
seats = [None]*(n**2+1)

for i in range(n**2):
    students.append(list(map(int, input().split())))    

# 자리 배정
for s in students:
    curr = s[0]
    like = s[1:5]       
    r, c = rule1(like)  
    room[r][c] = curr
    seats[curr] = (r, c)
    
# 만족도 계산
answer = 0
for i in range(0, n**2):
    r, c = seats[students[i][0]]
    like = students[i][1:5]
    temp = 0
    
    if r > 1 and room[r-1][c] in like:
        temp += 1
    if c < n and room[r][c+1] in like:
        temp += 1
    if r < n and room[r+1][c] in like:
        temp += 1
    if c > 1 and room[r][c-1] in like:
        temp += 1
        
    if temp > 0:
        answer += 10**(temp-1)
    
print(answer)