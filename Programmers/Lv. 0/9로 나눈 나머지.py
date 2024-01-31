def solution(number):
    # 각 자리 숫자의 합을 저장할 변수 sum
    sum = 0
    
    for num in str(number):
        sum += int(num)
    
    answer = sum % 9
    return answer
