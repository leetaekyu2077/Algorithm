import sys

n, r, c = map(int, sys.stdin.readline().split())
count = 0
row, col = 0, 0

def resursion(n, row, col, count):
    if n > 0:
        # 2사분면 범위에 있다면
        if r < row + 2**(n-1) and c < col + 2**(n-1):
            return resursion(n-1, row, col, count)
        # 1사분면 범위에 있다면
        elif r < row + 2**(n-1) and (c >= col + 2**(n-1) and c < col + 2**n):
            count += (2**n//2)**2
            return resursion(n-1, row, col + 2**(n-1), count)
        # 3사분면 범위에 있다면
        elif (r >= row + 2**(n-1) and r < row + 2**n) and c < col + 2**(n-1):
            count += (2**n//2)**2 * 2
            return resursion(n-1, row + 2**(n-1), col, count)
        # 4사분면 범위에 있다면
        else:
            count += (2**n//2)**2 * 3
            return resursion(n-1, row + 2**(n-1), col + 2**(n-1), count)
    else:
        return count
        
print(resursion(n, row, col, count))