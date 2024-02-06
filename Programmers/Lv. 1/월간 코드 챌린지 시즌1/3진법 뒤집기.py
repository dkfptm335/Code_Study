def solution(n):
    # 3진법으로 변환
    # n 이하의 가장 큰 3의 거듭제곱을 찾는다.
    i = 0
    
    while 3**i <= n:
        i += 1
    
    # i는 3진법의 자리수
    list_3 = [0] * i
    count = 0
    
    for j in range(i-1, -1, -1):
        list_3[count] = n // (3**j)
        n = n % (3**j)
        count += 1
        
    # 뒤집기
    list_3.reverse()
    
    # 10진법으로 변환
    answer = 0
    
    for k in range(len(list_3)):
        answer += list_3[k] * (3**(count-1))
        count -= 1
        
    return answer
    