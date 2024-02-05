def solution(x, n):
    answer = []
    sum = 0
    
    for i in range(n):
        sum += x
        answer.append(sum)
        
    return answer
