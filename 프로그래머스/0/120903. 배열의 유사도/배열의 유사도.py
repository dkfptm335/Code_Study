def solution(s1, s2):
    count = 0
    
    for val_1 in s1:
        for val_2 in s2:
            if val_1 == val_2:
                count += 1
                
    return count