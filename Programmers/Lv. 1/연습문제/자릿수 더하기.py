def solution(n):
    s = list(str(n))
    answer = 0
    
    for val in s:
        answer += int(val)
        
    return answer
