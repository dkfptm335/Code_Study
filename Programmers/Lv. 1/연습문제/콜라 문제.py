def solution(a, b, n):
    # a: 콜라를 받기 위해 마트에 주어야 하는 병 수
    # b: 빈 병 a개를 가져다주면 받을 수 있는 병 수
    # n: 현재 가지고 있는 병 수
    
    # 서비스 콜라의 개수
    service = 0
    
    while n >= a:
        service += n // a * b
        n = n // a * b + n % a
    
    return service
