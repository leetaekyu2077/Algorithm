n = int(input())

for i in range(0, n):
    nums = list(map(int, (input()).split()))
    gcd = 0

    for j in range(1, nums[0]):
        for k in range(j+1, nums[0]+1):
            a = nums[k]
            b = nums[j]
            while b != 0:
                a = a%b
                a,b = b,a
            gcd += a     
    print(gcd)