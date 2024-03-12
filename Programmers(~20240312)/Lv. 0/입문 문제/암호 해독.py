def solution(cipher, code):
    answer = ''
    
    for i in range(-1, len(cipher), code):
        if i == -1:
            pass
        else:
            answer += cipher[i]
    
    return answer
