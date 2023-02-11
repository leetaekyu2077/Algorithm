import sys
input = sys.stdin.readline

n = 1000000
all_prime = [True]*(n+1)
m = int(n**0.5)

for i in range(3, m+1, 2):
    if all_prime[i] == True:
        for j in range(i*2, n+1, i):
            all_prime[j] = False

while True:
    n = int(input())
    flag = True
    
    if n > 0:
        for i in range(3, n//2+1, 2):
            if all_prime[i] and all_prime[n-i]:
                print('{} = {} + {}'.format(n, i, n-i))
                flag = False
                break
        
        if flag:
            print("Goldbach's conjecture is wrong.")
    else:
        break