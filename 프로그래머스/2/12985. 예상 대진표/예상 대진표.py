def solution(n,a,b):
    if max(a, b) % 2 == 0 and abs(a-b) == 1:
        return 1
    round = 0
    
    while True:
        if max(a, b) % 2 == 0 and abs(a-b) == 1:
            break
            
        round += 1
        
        if a % 2 == 1:
            a = (a + 1) // 2
        else:
            a //= 2
            
        if b % 2 == 1:
            b = (b + 1) // 2
        else:
            b //= 2
        
    return round+1