import sys
input = sys.stdin.readline
            
n = int(input())
records = [0]*(n+1)
squares = [i**2 for i in range(int(n**0.5+1))]

for i in range(1, n+1):    
    min = sys.maxsize
    for j in range(1, int(i**0.5)+1):  
        temp = records[i-squares[j]]
        if temp < min:
            min = temp
    
    records[i] = min+1

print(records[n])