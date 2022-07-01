import sys

#에라토스테네스의 체
n = 1000
all_prime=[True]*(n+1)
all_prime[1] = False
m = int(n**0.5)

for i in range(2, m+1):
    if all_prime[i] == True:
        for j in range(i+i,n+1,i):
            all_prime[j] = False

n = int(input())
nums = list(map(int, input().split()))
primes = 0

for i in nums:
    if all_prime[i] == True:
        primes += 1
print(primes)