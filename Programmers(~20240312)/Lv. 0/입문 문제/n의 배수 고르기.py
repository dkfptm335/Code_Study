def solution(n, numlist):
    answer = []
    
    # numlist에서 n의 배수만 answer에 추가
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    
    return answer
