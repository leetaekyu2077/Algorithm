import sys
input = sys.stdin.readline

n = int(input())
answer = 0
schedules = []

for _ in range(n):
    schedules.append(tuple(map(int, input().split())))
  
schedules.sort(key=lambda x: (x[0], -x[1]))
start, end = 0, -1
records = []

for i in range(n):
    s, e = schedules[i]
    if s <= end+1:   
        found = False
        for j in range(len(records)):
            if records[j] < s:   
                found = True
                records[j] = e
                break
            
        if not found:
            records.append(e)
            
        if end < e:
            end = e
    
    else:
        answer += len(records)*(end - start + 1)
        start, end = schedules[i][0], schedules[i][1]
        records = [schedules[i][1]]
    
answer += len(records)*(end - start + 1)  
print(answer)