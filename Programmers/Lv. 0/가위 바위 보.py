# 가위는 2 바위는 0 보는 5

def solution(rsp):
    answer = ''
    
    for val in rsp:
        if val == '2':
            answer += '0'
        elif val == '0':
            answer += '5'
        elif val == '5':
            answer += '2'
    
    return answer
