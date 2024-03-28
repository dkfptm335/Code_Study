def solution(array):
    answer = []
    
    # 가장 큰 수와 그 수의 인덱스를 담은 배열을 return
    answer.append(max(array))
    answer.append(array.index(max(array)))
                      
    return answer
