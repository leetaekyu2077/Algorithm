import sys

#에라토스테네스의 체
n = 1000000
all_prime=[True]*(n+1)
m = int(n**0.5)

for i in range(2, m+1):
    if all_prime[i] == True:
        for j in range(i+i,n+1,i):
            all_prime[j] = False

n = int(input())

while n!=0:
    for i in range(2, m+1):
        if all_prime[i] == True:
            if all_prime[n-i] == True:
                print('{} = {} + {}'.format(n, i, n-i))
                break
    n = int(input())