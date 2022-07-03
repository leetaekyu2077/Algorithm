s = list(input())
std = 'quack'
lst = []

if s[0] == 'q': 
    lst.append(1)
else: 
    print(-1)
    exit()
    
for i in range(1, len(s)):
    for j in range(len(lst)):
        if std[lst[j]] == s[i]:
            lst[j] += 1
            if lst[j] == 5:
                lst[j] = 0
            break
        else:
            if j == len(lst) - 1:
                lst.append(1)

if sum(lst) == 0:
    print(len(lst))  
else:
    print(-1)  