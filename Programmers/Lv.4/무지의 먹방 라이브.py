import heapq

def solution(food_times, k):
    answer = -1
    times = []
    t = 0
    previous = 0
    # 모든 요소 heap에 삽입
    for i in range(len(food_times)):
        heapq.heappush(times, (food_times[i], i + 1))
        
    # 더 이상 먹을 음식이 없으면 return -1   
    while times:
        min_time = times[0][0] - previous
        if t + min_time * len(times) <= k:
            t += min_time * len(times)
            previous = heapq.heappop(times)[0]
        # 남은 시간이 먹는 시간보다 짧을 때
        else:
            times.sort(key=lambda x:x[1])
            answer = times[(k-t)%len(times)][1]
            return answer
                
    return answer