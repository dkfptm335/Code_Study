def solution(lottos, win_nums):
    
    correct = 0
    
    for num in lottos:
        if num in win_nums:
            correct += 1
            
    zero = lottos.count(0)
    
    answer = []
    
    answer.append(7 - (correct + zero))
    answer.append(7 - correct)
    
    for i in range(2):
        if answer[i] == 7:
            answer[i] = 6
    
    return answer
