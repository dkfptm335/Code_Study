def get_measure_count(num):
    measure_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            measure_count += 1
            
    return measure_count

def solution(left, right):
    sum = 0
    
    for num in range(left, right + 1):
        if get_measure_count(num) % 2 == 0:
            sum += num
        else:
            sum -= num
    
    return sum
