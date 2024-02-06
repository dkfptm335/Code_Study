def solution(my_string):
    answer = []
    
    for num in my_string:
        if num.isdigit():
            answer.append(int(num))
            
    answer.sort()
    
    return answer
