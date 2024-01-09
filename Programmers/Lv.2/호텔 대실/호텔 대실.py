def solution(book_time):
    times = []
    for s, e in book_time:
        sh, sm = map(int, s.split(':'))
        eh, em = map(int, e.split(':'))
        start, end = sh*60+sm, eh*60+em+10
        times.append((start, end))

    times.sort(key=lambda x: x[0])
    rooms = [[times[0]]]
    for t in times[1:]:
        idx = len(rooms)
        min = 1440
        for i in range(0, len(rooms)):
            if rooms[i][1] <= t[0] and min > rooms[i][1]:
                min = rooms[i][1]
                idx = i
                
        if idx < len(rooms):
            rooms[idx] = t
        else:
            rooms.append(t)

    return len(rooms)

print(solution(	[["09:10", "10:10"], ["10:20", "12:20"]]))