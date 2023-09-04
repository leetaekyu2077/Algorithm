def solution(m, n, board):
    answer = 0
    flag = True

    board = [list(line) for line in board]
    removed = [['.']*n for _ in range(m)]

    def check(i, j):
        nonlocal answer

        if (board[i][j] == board[i+1][j] == 
            board[i][j+1] == board[i+1][j+1]):

            removed[i][j] = '-'
            removed[i+1][j] = '-'
            removed[i][j+1] = '-'
            removed[i+1][j+1] = '-'

            return True
        
        return False

    # 아래 쪽으로 블록을 몰아놓는 방식으로 수정하기
    def drop(c, col):
        dropped = [b for b in col if b != '-'][::-1]
        dropped.extend(['-']*(m-len(dropped)))
        
        for i, block in enumerate(dropped[::-1]):
            board[i][c] = block

    while flag:
        flag = False
        removed = [['.']*n for _ in range(m)]

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-':
                    if check(i, j):
                        flag = True
    
        for i in range(m):
            for j in range(n):
                if removed[i][j] == '-':
                    board[i][j] = '-'

        if flag:
            for i, col in enumerate(list(map(list, zip(*board)))): 
                drop(i, col)

    for line in board:
        answer += line.count('-')

    return answer

print(solution(6, 6, ['IIIIOO', 'IIIOOO', 'IIIOOI', 'IOOIII', 'OOOIII', 'OOIIII']))

# '---I--'
# '------'
# '-----I'
# 'I-----'
# '------'
# '--I---'