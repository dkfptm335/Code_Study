def solution(numbers):
    # numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값
    max_max = 0
    max_min = 0
    
    numbers.sort()
    
    max_min = numbers[0] * numbers[1]
    max_max = numbers[-1] * numbers[-2]
    
    return max_max if max_max >= max_min else max_min
