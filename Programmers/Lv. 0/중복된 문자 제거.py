def solution(my_string):
    answer = ''
    
    char_list = []
    
    for char in my_string:
        if char not in char_list:
            char_list.append(char)
            answer += char
        else:
            pass
    
    return answer
