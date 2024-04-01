def solution(elements):
    sums = []
    
    # 시작 지점, 크기
    
    for idx in range(len(elements)):
        for size in range(1, len(elements) + 1):
            if idx + size > len(elements):
                sums.append(sum(elements[idx:] + elements[:idx + size - len(elements)]))
            else:
                sums.append(sum(elements[idx: idx + size]))
                
    return len(set(sums))