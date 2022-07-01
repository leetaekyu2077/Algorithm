def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report = list(set(report))
    report_person = {'unknown': []}
    report_count = {'unknown': 0}
    result = {'unknown': 0}
    for id in id_list:
        result[id] = 0
    
    for item in report:
        a, b = item.split()
        if b in report_person:
            report_person[b].append(a)
            report_count[b] += 1
        else:
            report_person[b] = [a]
            report_count[b] = 1
            
    for person, count in report_count.items():
        if count >= k:
            for a in report_person[person]:
                if a in result:
                    result[a] += 1
                else:
                    result[a] = 1
                
    for i in range(len(id_list)):
        answer[i] = result[id_list[i]]
        
    return answer