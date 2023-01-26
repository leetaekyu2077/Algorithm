import sys
from itertools import combinations
input = sys.stdin.readline

t = input().strip()
n = int(input())
books = []

for _ in range(n):
    price, name = input().split()
    books.append((int(price), name))

comb = []
for i in range(1, n+1):
    for case in combinations(books, i):
        temp_price = 0
        temp_name = ''
        for price, name in case:
            temp_price += price
            temp_name += name
        comb.append((temp_price, temp_name))
comb.sort()

for price, name in comb:
    found = [False]*len(t)
    for c in name:
        for j in range(len(t)):
            if not found[j] and c == t[j]:
                found[j] = True
                break
    
    if all(found):
        print(price)
        exit(0)     
                          
print(-1)        