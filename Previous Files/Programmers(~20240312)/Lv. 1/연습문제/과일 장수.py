def solution(k, m, score):
    
    sum = 0
    
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            sum += min(score[i:i+m]) * m
        
    return sum
