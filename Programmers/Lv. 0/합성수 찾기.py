def count_measures(n):
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        return count

def solution(n):
    answer = 0

    for i in range(1, n+1):
        if count_measures(i) >= 3:
            answer += 1
            
    return answer
