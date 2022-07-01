# from collections import defaultdict

def solution(record):
    answer = []
    # user_list = defaultdict(str)
    user_list = {'admin': 'admin'}
    for message in record:
        tokens = message.split()
        if tokens[0] == 'Enter' or tokens[0] == 'Change':
            user_list[tokens[1]] = tokens[2]
    
    for message in record:
        tokens = message.split()
        if tokens[0] == 'Enter':
            answer.append(user_list[tokens[1]]+'님이 들어왔습니다.')
        if tokens[0] == 'Leave':
            answer.append(user_list[tokens[1]]+'님이 나갔습니다.')
    return answer