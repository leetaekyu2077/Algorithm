n = int(input())

for i in range(0, n):
    a,b = map(int, (input()).split())

    A, B = a, b
    2
    while b != 0:
        a = a%b
        a,b = b,a

    print(A*B//a)