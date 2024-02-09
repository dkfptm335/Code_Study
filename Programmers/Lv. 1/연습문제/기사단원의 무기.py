def get_measure_count(n):
    measure_count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            measure_count += 1
            if n // i != i:
                measure_count += 1
    
    return measure_count


def solution(number, limit, power):
    knights = [get_measure_count(i) for i in range(1, number+1)]
    
    for i in range(len(knights)):
        if knights[i] > limit:
            knights[i] = power

    return sum(knights)
