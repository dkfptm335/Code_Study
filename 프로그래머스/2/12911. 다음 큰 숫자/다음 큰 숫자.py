def solution(n):
    # 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
    # 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
    # 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
    
    # 다음 큰 숫자
    next = 0
    tmp = n + 1
    n_bin_one = bin(n).count("1")
    
    while not next:
        if bin(tmp).count("1") == n_bin_one:
            next = tmp
            break
        else:
            tmp += 1
            
    return next

        