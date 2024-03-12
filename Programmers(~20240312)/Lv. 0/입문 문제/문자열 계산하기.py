def solution(my_string):
    answer = 0
    
    list_op = my_string.split(' ')
    
    for i in range(len(list_op)-1):
        if i == 0:
            answer = int(list_op[i])
        else:
            if list_op[i] == '+':
                answer += int(list_op[i+1])
            elif list_op[i] == '-':
                answer -= int(list_op[i+1])
            else:
                pass
    
    return answer
