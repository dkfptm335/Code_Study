def solution(before, after):
    before_list = list(before)
    after_list = list(after)
    
    before_list.sort()
    after_list.sort()
    
    return 1 if before_list == after_list else 0
