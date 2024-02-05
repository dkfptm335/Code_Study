def operation(str):
    operrand = str.split(' ')
    
    if operrand[1] == '+':
        return int(operrand[0]) + int(operrand[2])
    else:
        return int(operrand[0]) - int(operrand[2])
    
def check(str):
    check_list = str.split('=')
    
    for i in range(len(check_list)):
        check_list[i] = check_list[i].strip()
    
    if operation(check_list[0]) == int(check_list[1]):
        return 'O'
    else:
        return 'X'
    
def solution(quiz):
    answer = []
    
    for q in quiz:
        answer.append(check(q))
    
    return answer
