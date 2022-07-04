from functools import cmp_to_key
import sys

def xy_compare(x, y):
    if x[1] < y[1]:
        return 1
    elif x[1] > y[1]:
        return -1
    else:
        if x[2] > y[2]:
            return 1
        elif x[2] < y[2]:
            return -1
        else:
            if x[3] < y[3]:
                return 1
            elif x[3] > y[3]:
                return -1
            else:
                if x[0] > y[0]:
                    return 1
                else:
                    return -1

scores = []
n = int(sys.stdin.readline())
for i in range(n):
    temp = sys.stdin.readline().split()
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    scores.append(temp)

result = sorted(scores, key=cmp_to_key(xy_compare))
for line in result:
    sys.stdout.write(line[0]+'\n')