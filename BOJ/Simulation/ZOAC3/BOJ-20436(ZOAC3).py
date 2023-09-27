import sys

left, right = sys.stdin.readline().split()
string = sys.stdin.readline().strip()
border = 4
key_location = dict()
keyboard = [
    list(map(str, 'qwertyuiop')),
    list(map(str, 'asdfghjkl')),
    list(map(str, 'zxcvbnm'))
]

for i, line in enumerate(keyboard):
    for j, c in enumerate(line):
        key_location[c] = (i, j)

# 초기 설정
time = 0
l_hand = key_location[left]
r_hand = key_location[right]

for c in string:
    loc = key_location[c]
    # 오른손
    if loc[1] > 4 or c == 'b':
        time += abs(r_hand[0] - loc[0]) + abs(r_hand[1] - loc[1]) + 1
        r_hand = loc
    # 왼손
    else:
        time += abs(l_hand[0] - loc[0]) + abs(l_hand[1] - loc[1]) + 1
        l_hand = loc
print(time)