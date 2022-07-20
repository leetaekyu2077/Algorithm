height = []

for i in range(0,9):
    height.append(int(input()))

heights_sum = sum(height)
height.sort()

for i in range(9):
    for j in range(i+1,9):
        if heights_sum-(height[i]+height[j]) == 100:
            for k in range(9):
                if k==i or k==j:
                    continue
                else:
                    print(height[k])
            exit()