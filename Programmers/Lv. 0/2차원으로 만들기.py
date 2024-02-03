def solution(num_list, n):
    answer = []
    
    for i in range(len(num_list) // n):
        tmp = []
        for j in range(n):
            tmp.append(num_list[i * n + j])
        answer.append(tmp)
    
    return answer
