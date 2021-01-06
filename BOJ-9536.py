n = int(input())

for i in range(0,n):
    sounds = str(input()).split()

    line = input()

    while line != 'what does the fox say?':
        temp = line.split()
        num = 0
        for i in range(0,sounds.count(temp[2])):
                sounds.remove(temp[2])
        line = input()

    result = ' '.join(sounds)
    print(result)

