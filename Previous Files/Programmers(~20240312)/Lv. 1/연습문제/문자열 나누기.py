def solution(s):
    splited = 0
    
    same = 0
    diff = 0
    
    for char in s:
        if same == diff:
            splited += 1
            same = 0
            diff = 0
            x = char
            
        if x == char:
            same += 1
        else:
            diff += 1
            
    
    return splited
