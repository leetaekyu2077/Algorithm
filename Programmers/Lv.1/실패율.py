def solution(N, stages):
    answer = []
    failure = [[i+1,0] for i in range(N)]
    cleared = len(stages)
    for i in range(N):
        now = stages.count(i+1)
        if cleared != 0:
            failure[i][1] = now / cleared
            cleared -= now
        else:
            failure[i][1] = 0
        
    failure.sort(key=lambda x:x[1], reverse=True)
    for stage in failure:
        answer.append(stage[0])
    return answer