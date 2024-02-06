def solution(s):
    answer = 0
    
    operrand = s.split()
    
    for i in range(len(operrand)):
        if i == 0:
            answer = int(operrand[i])
        elif operrand[i] == 'Z':
            answer -= int(operrand[i-1])
        else:
            answer += int(operrand[i])
    
    return answer
