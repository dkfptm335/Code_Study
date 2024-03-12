def solution(arr):
    answer = []
    
    for val in arr:
        if len(answer) == 0:
            answer.append(val)
        elif answer[-1] != val:
            answer.append(val)
    
    return answer
