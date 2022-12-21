import sys
import heapq

N = int(sys.stdin.readline())

min_heap = []
max_heap = []
problems = dict()

for _ in range(N):
    p, l = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    problems[p] = l
    
M = int(sys.stdin.readline())

for _ in range(M):
    commands = list(sys.stdin.readline().split())
    
    if commands[0] == 'add':
        # 문제 리스트와 각 우선순위 큐에 추가
        problems[int(commands[1])] = int(commands[2])
        heapq.heappush(min_heap, (int(commands[2]), int(commands[1])))
        heapq.heappush(max_heap, (-int(commands[2]), -int(commands[1])))
    elif commands[0] == 'solved':
        # 문제 리스트에서 제거
        del(problems[int(commands[1])])
    else:
        # 제거된 문제를 만나면 pop, 아니면 출력
        if commands[1] == '-1':
            while min_heap[0][1] not in problems or problems[min_heap[0][1]] != min_heap[0][0]:
                heapq.heappop(min_heap)
            print(min_heap[0][1])
        else:
            while -max_heap[0][1] not in problems or problems[-max_heap[0][1]] != -max_heap[0][0]:
                heapq.heappop(max_heap)
            print(-max_heap[0][1])