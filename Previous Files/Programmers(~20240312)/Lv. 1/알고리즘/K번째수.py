def solution(array, commands):
    answer = []
    
    # commands = [[i, j, k], [i, j, k], ...]
    # 인덱스 기준으로 i-1 j-1까지 자르고[i-1:j] 정렬한 후 k-1번째 수를 answer에 추가
    
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer
