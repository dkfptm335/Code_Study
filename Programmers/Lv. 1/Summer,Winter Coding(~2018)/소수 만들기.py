def get_measure_count(n):
    measure_count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            measure_count += 1
            if n // i != i:
                measure_count += 1
    
    return measure_count

def is_prime(n):
    if get_measure_count(n) == 2:
        return True
    else:
        return False
    
def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime(nums[i] + nums[j] + nums[k]):
                    answer += 1
                    
    return answer
