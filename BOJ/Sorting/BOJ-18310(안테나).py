import sys
    
n = int(sys.stdin.readline())
antena = list(map(int, sys.stdin.readline().split()))
antena.sort()

print(antena[(len(antena)-1)//2])