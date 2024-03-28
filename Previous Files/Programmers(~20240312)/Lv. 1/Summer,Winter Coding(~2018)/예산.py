def solution(d, budget):
    d.sort()
    
    supplied = []
    
    while len(d) != 0:
        # 지원 가능한가?
        if sum(supplied) + d[0] <= budget:
            supplied.append(d.pop(0))
        else:
            break
        
    return len(supplied)


# d            supplied
# 2 2 3 3      
# 2 3 3        2
# 3 3          2 2
# 3            2 2 3
#              2 2 3 3
