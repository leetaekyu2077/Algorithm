import sys
input = sys.stdin.readline

def operation1():
    global table
    table = table[::-1]

def operation2():
    global table
    for i, line in enumerate(table):
        table[i] = line[::-1]

def operation3():
    global table, n, m
    n, m = m, n
    table = list(map(list, zip(*table)))
    operation2()

def operation4():
    global table, n, m
    n, m = m, n
    operation2()
    table = list(map(list, zip(*table)))

def operation5():
    global table
    n_half = n//2
    group1, group2, group3, group4 = get_groups()

    table[:n_half] = [group4[i] + group1[i] for i in range(n_half)]
    table[n_half:] = [group3[i] + group2[i] for i in range(n_half)]

def operation6():
    global table
    n_half = n//2
    group1, group2, group3, group4 = get_groups()

    table[:n_half] = [group2[i] + group3[i] for i in range(n_half)]
    table[n_half:] = [group1[i] + group4[i] for i in range(n_half)]
    
def get_groups():
    n_half, m_half = n//2, m//2

    group1 = [table[i][:m_half] for i in range(n_half)]
    group2 = [table[i][m_half:] for i in range(n_half)]
    group3 = [table[i][m_half:] for i in range(n_half, n)]
    group4 = [table[i][:m_half] for i in range(n_half, n)]

    return group1, group2, group3, group4

# 메인
n, m, r = map(int, input().split())

table = []
for _ in range(n):
    table.append(list(map(int, input().split())))

operations = list(map(int, input().split()))

for op in operations:
    if op == 1: operation1()
    elif op == 2: operation2()
    elif op == 3: operation3()
    elif op == 4: operation4()
    elif op == 5: operation5()
    else: operation6()

for line in table:
    print(*line, sep=' ')