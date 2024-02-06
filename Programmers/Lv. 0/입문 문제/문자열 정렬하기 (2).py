def solution(my_string):
    my_string = my_string.lower()
    my_list = list(my_string)
    my_list.sort()
    
    return ''.join(my_list)
