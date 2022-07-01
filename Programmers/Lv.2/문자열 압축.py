def solution(s):
    l = len(s)//2
    min = len(s)

    for size in range(l, 0, -1):
        result = len(s)
        index = 1
        count = 0
        lst = [s[i:i+size] for i in range(0, len(s), size)]
        pattern = lst[0]
        while index < len(lst):
            if pattern == lst[index]:
                count += 1
                index += 1
            else:
                if count != 0:
                    result = result - size*count + len(str(count+1))
                pattern = lst[index]
                count = 0
                index += 1

        if count != 0:
                result = result - size*count + len(str(count+1))
        if min > result:
            min = result
    return min