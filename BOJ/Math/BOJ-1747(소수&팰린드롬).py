import sys
input = sys.stdin.readline
n = int(input())

if n == 1:
    n += 1

def isPalindrome(num):
    length = len(num)
    for i in range(length//2):
        if num[i] != num[length-i-1]:
            return False
    return True

def isPrime(num):
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

while True:
    if isPalindrome(str(n)):
        if isPrime(n):
            break
    n += 1
print(n)