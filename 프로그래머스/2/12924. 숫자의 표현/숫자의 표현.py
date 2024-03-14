def solution(n):
    answer = 0
    
    for k in range(1, int((2*n)**0.5)+1):
        if(2*n - k*(k+1)) % (2*k) == 0:
            answer += 1
            
    return answer
