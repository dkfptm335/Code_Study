def solution(lines):
    # lines: [[start, end], [start, end], [start, end]]
    # start의 min, end의 max를 구하고 list선언
    start_min = 100
    end_max = -100
    
    for line in lines:
        start_min = min(start_min, line[0])
        end_max = max(end_max, line[1])
        
    list_range = [0] * (end_max - start_min)
    
    for line in lines:
        for i in range(line[0], line[1]):
            list_range[i - start_min] += 1
            
    value = 0
    
    for val in list_range:
        if val > 1:
            value += 1
            
    return value
