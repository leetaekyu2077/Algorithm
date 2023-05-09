import sys
input = sys.stdin.readline

n = int(input())
colors = input().rstrip()

temp = ''
while len(temp) != len(colors):
    temp = colors
    colors = colors.replace('BB', 'B').replace('RR', 'R') 

cnt = colors.count('B')
print(min(cnt, len(colors)-cnt)+1)