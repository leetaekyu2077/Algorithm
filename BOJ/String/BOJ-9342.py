import sys, re
input = sys.stdin.readline

n = int(input())
p = re.compile('^[A-F]?A+F+C+[A-F]?$')
print(*['Good' if p.match(input().rstrip()) == None else 'Infected!' for _ in range(n)], sep='\n')