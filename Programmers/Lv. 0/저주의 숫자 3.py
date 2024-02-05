def no3_num(num):
    if '3' in str(num):
        return True
    elif num % 3 == 0:
        return True
    else:
        return False

def solution(n):
    no3_num_list = []
    
    i = 0
    
    while len(no3_num_list) < n:
        i += 1
        
        while no3_num(i):
            i += 1
        
        no3_num_list.append(i)
            
        
        
    return no3_num_list[len(no3_num_list) - 1]
