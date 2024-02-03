# 문제 설명
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

def solution(array, n):
    answer = 0
    
    sub = []
    
    for val in array:
        sub.append(abs(val - n))
    
    min_value = min(sub)
    if sub.count(min_value) > 1:
        tmp = []
        for i in range(len(sub)):
            if sub[i] == min_value:
                tmp.append(array[i])
        answer = min(tmp)
    else:
        answer = array[sub.index(min_value)]
    
    return answer
