def convert(p):    
    # 올바른 문자열이 아닐 때만
    if not isCorrect(p):
        u, v = '', ''
        std = ''
        result = ''
        std = p[0]
        count = 1
        # 앞에서부터 최소의 균형잡힌 문자열 찾기
        for i in range(1, len(p)):
            if p[i] == std:
                count += 1
            else:
                count -= 1
                if count == 0:
                    u = p[:i+1]
                    v = p[i+1:]
                    break
        
        if isCorrect(u):
            result += u + convert(v)
        else:
            result = '(' + convert(v) + ')'
            temp = u[1:len(u)-1]
            sub = ''
            for c in temp:
                if c == ')': 
                    sub += '('
                elif c == '(': sub += ')'   
            result += sub            
    
    else: 
        result = p  
    
    return result
    
def isCorrect(u):
    if len(u) > 0:
        stk = 0
        for c in u:
            if c == '(': 
                stk += 1
            elif c == ')' and stk > 0:
                stk -= 1
            else:
                return False
        if stk > 0:
            return False
    return True

def solution(p):
    answer = convert(p)
    return answer

def main():
    print(solution(input()))
    
if __name__ == "__main__":
    main()    