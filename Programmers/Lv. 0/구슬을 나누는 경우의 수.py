def solution(balls, share):
    numerator = 1
    denominator = 1
    
    # 서로 다른 balls 중 share개를 뽑는 경우의 수
    # balls combination share
    
    # nCr = nCn-r
    
    share = min(share, balls-share)
    
    for i in range(share):
        numerator *= balls-share+1+i
        denominator *= i+1
        
    answer = numerator//denominator
    
    return answer
