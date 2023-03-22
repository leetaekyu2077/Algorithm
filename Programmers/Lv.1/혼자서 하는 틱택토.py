def count(board):
    cnt_o, cnt_x = 0, 0
    line_o, line_x = 0, 0
    
    # O, X 갯수 세기
    for line in board:
        cnt_o += line.count('O')
        cnt_x += line.count('X')
    
    # 가로줄 완성 세기
    for line in board:
        if line == 'OOO': 
            line_o += 1
        if line == 'XXX':
            line_x += 1
    
    # 세로줄 완성 세기
    for line in zip(*board):
        if ''.join(line) == 'OOO':
            line_o += 1
        if ''.join(line) == 'XXX':
            line_x += 1
    
    # 대각선 완성 세기
    if (board[0][0]+board[1][1]+board[2][2] == 'OOO' or
        board[0][2]+board[1][1]+board[2][0] == 'OOO'):
        line_o += 1
    if (board[0][0]+board[1][1]+board[2][2] == 'XXX' or
        board[0][2]+board[1][1]+board[2][0] == 'XXX'):
        line_x += 1
        
    return cnt_o, cnt_x, line_o, line_x

def solution(board):
    cnt_o, cnt_x, line_o, line_x = count(board)
    print(cnt_o, cnt_x, line_o, line_x)
    
    # X의 갯수가 더 많은 경우
    if cnt_o < cnt_x:
        return 0
    # 완성된 O 라인이 둘 이상인 경우
    if line_o > 2:
        if not (cnt_o == 5 and cnt_x == 4):
            return 0      
    # O, X 갯수 차이가 2 이상인 경우
    if abs(cnt_o - cnt_x) > 1:
        return 0
    # O가 승리했는데 X의 갯수가 더 많을 때
    if line_o > 0 and cnt_o <= cnt_x:
        return 0
    # X가 승리했는데 O의 갯수가 더 많을 때
    if line_x > 0 and cnt_o > cnt_x:
        return 0
        
    return 1