def solution(s):
    str = list(s.lower())
    num_p = 0
    num_y = 0
    
    for val in str:
        if val == 'p':
            num_p += 1
        if val == 'y':
            num_y += 1
    
    return True if num_p == num_y else False
