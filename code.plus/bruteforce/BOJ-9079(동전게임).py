import sys
from time import sleep

N = int(sys.stdin.readline())

table = []
queue = []
visited = []
all = []
answer = []

def row1(current):
    temp = [item[:] for item in current]
    temp[0][0] = not temp[0][0]
    temp[0][1] = not temp[0][1]
    temp[0][2] = not temp[0][2]
    return temp

def row2(current):
    temp = [item[:] for item in current]
    temp[1][0] = not temp[1][0]
    temp[1][1] = not temp[1][1]
    temp[1][2] = not temp[1][2]
    return temp

def row3(current):
    temp = [item[:] for item in current]
    temp[2][0] = not temp[2][0]
    temp[2][1] = not temp[2][1]
    temp[2][2] = not temp[2][2]
    return temp

def col1(current):
    temp = [item[:] for item in current]
    temp[0][0] = not temp[0][0]
    temp[1][0] = not temp[1][0]
    temp[2][0] = not temp[2][0]
    return temp

def col2(current):
    temp = [item[:] for item in current]
    temp[0][1] = not temp[0][1]
    temp[1][1] = not temp[1][1]
    temp[2][1] = not temp[2][1]
    return temp

def col3(current):
    temp = [item[:] for item in current]
    temp[0][2] = not temp[0][2]
    temp[1][2] = not temp[1][2]
    temp[2][2] = not temp[2][2]
    return temp

def diagonal1(current):
    temp = [item[:] for item in current]
    temp[0][0] = not temp[0][0]
    temp[1][1] = not temp[1][1]
    temp[2][2] = not temp[2][2]
    return temp
    
def diagonal2(current):
    temp = [item[:] for item in current]
    temp[0][2] = not temp[0][2]
    temp[1][1] = not temp[1][1]
    temp[2][0] = not temp[2][0]
    return temp
    
def isSame(current, lst):
    for i, table in enumerate(lst):
        for j in range(3):
            if (current[j][0] != table[j][0] or 
                current[j][1] != table[j][1] or 
                current[j][2] != table[j][2]): break
            if j == 2: return True, i
    return False, -1
    
def check_complete(current):
    std = current[0][0]
    for line in current:
        for item in line:
            if item != std:
                return False
    return True

def main():
    for i in range(N):
        table = []
        queue = []
        visited = []
        all = []
        cnt = 0
        for j in range(3):
            temp = list(map(str, sys.stdin.readline().split()))
            for k, item in enumerate(temp):
                if item == 'H': temp[k] = True
                elif item == 'T': temp[k] = False
            table.append(temp)
            
        queue.append(table)
        
        while len(queue) > 0:
            cnt += 1
            current = queue.pop(0)
            all.append(current)
            if check_complete(current) == True:
                break
            flag, _ = isSame(current, visited)
            if flag == False:
                visited.append(current)
                queue.append(row1(current))
                queue.append(row2(current))
                queue.append(row3(current))
                queue.append(col1(current))
                queue.append(col2(current))
                queue.append(col3(current))
                queue.append(diagonal1(current))
                queue.append(diagonal2(current))
                
        result = 0
        if len(queue) > 0:
            step = cnt-1
            flag = flag, _ = isSame(current, [table])
            while flag != True:
                prior_move = step % 8
                if prior_move == 1: current = row1(current)
                elif prior_move == 2: current = row2(current)
                elif prior_move == 3: current = row3(current)
                elif prior_move == 4: current = col1(current)
                elif prior_move == 5: current = col2(current)
                elif prior_move == 6: current = col3(current)
                elif prior_move == 7: current = diagonal1(current)
                elif prior_move == 0: current = diagonal2(current)
                
                result += 1
                _, step = isSame(current, all)
                flag, _ = isSame(current, [table])
            
            print(result)

        elif cnt == 1:
            print(0)
        else:
            print(-1)
                
if __name__=="__main__": 
    main()