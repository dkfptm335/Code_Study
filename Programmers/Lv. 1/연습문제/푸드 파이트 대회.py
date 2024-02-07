def solution(food):
    answer = ''
    
    # 1. index 1부터 마지막까지 홀수라면 1씩 빼기
    # 2. index 1부터 마지막까지 각 요소의 1/2만큼 인덱스 붙여서 문자열로 만들기
    # 3. 완성
    
    for i in range(1, len(food)):
        if food[i] % 2:
            food[i] -= 1
            
    tmp = ''
    
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            tmp += str(i)
            
    answer = tmp + '0' + tmp[::-1]
    
    return answer
