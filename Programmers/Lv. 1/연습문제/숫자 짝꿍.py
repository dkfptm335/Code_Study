from collections import Counter

def solution(X, Y):
    
    counter_x = Counter(X)
    counter_y = Counter(Y)
    
    common = counter_x & counter_y
    
    common_list = list(common.elements())
    
    common_list.sort(reverse=True)
    
    common_list = ''.join(common_list)
    
    if len(common_list) == 0:
        return '-1'
    elif len(common_list) == common_list.count('0'):
        return '0'
    else:
        return common_list
    