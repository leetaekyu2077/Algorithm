import sys

n = int(sys.stdin.readline())
options = []
short_cuts = []
for i in range(n):
    options.append((sys.stdin.readline().rstrip()))

results = [-1 for _ in range(len(options))]
for i in range(len(options)): 
    flag = False
    for j in range(len(options[i])):
        if j == 0 or options[i][j-1] == ' ':
            if options[i][j] != ' ' and options[i][j] not in short_cuts:
                short_cuts.append(str(options[i][j]).upper())
                short_cuts.append(str(options[i][j]).lower())
                results[i] = j
                flag = True
                break
    if not flag:
        for j in range(len(options[i])):
            if options[i][j] != ' ' and options[i][j] not in short_cuts: 
                short_cuts.append(str(options[i][j]).upper())
                short_cuts.append(str(options[i][j]).lower())
                results[i] = j
                break
                
for i in range(len(options)):
    if results[i] != -1:
        temp = list(options[i])
        temp.insert(results[i], '[')
        if results[i] == len(options[i]) - 1:
            temp.append(']')
        else:
            temp.insert(results[i]+2, ']')
        print(''.join(temp))
    else:
        print(options[i])