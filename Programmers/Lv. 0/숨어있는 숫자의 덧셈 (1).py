def solution(my_string):
    answer = 0
    
    for val in my_string:
        if val.isdigit():
            answer += int(val)
    
    return answer
