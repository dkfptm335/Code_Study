# 소인수는 소수인 인수이다.
# 소수는 1과 자기자신만을 약수로 가지는 수이다.
# 자연수의 인수는 약수와 동일하다.
# 약수를 구한 후 약수의 개수가 2개인지 확인한다.

def get_measure_count(n):
    measure = 0
    for i in range(1, n+1):
        if n % i == 0:
            measure += 1
    return measure

def get_prime_number(n):
    prime = []
    
    for i in range(1, n+1):
        if n % i == 0:
            if get_measure_count(i) == 2:
                prime.append(i)
                
    return prime


def solution(n):
    prime_measure = sorted(get_prime_number(n))
    return prime_measure
